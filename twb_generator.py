#!/usr/bin/env python3
"""
Tableau .twb XML Generator
Generates complete Tableau workbook XML from specifications
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent

class TWBGenerator:
    def __init__(self):
        self.spec = json.load(open(ROOT / 'dashboard_spec.json'))
        self.data_spec = self.load_data_spec()
    
    def load_data_spec(self):
        import yaml
        with open(ROOT / 'data_spec.yaml') as f:
            return yaml.safe_load(f)
    
    def build(self):
        # Root workbook element
        wb = ET.Element('workbook', {
            'version': '2023.4',
            'source-platform': 'win',
            'source-build': '2023.4.0'
        })
        
        # Add datasource
        wb.append(self.build_datasource())
        
        # Add worksheets
        for sheet_spec in self.spec['sheets']:
            wb.append(self.build_worksheet(sheet_spec))
        
        # Add dashboard
        wb.append(self.build_dashboard())
        
        # Pretty print
        rough = ET.tostring(wb, 'utf-8')
        reparsed = minidom.parseString(rough)
        return reparsed.toprettyxml(indent="  ")
    
    def build_datasource(self):
        ds = ET.Element('datasource', {
            'name': 'supermarket_sales',
            'caption': 'Supermarket Sales',
            'inline': 'true',
            'version': '2023.4'
        })
        
        # Connection
        conn = ET.SubElement(ds, 'connection', {
            'class': 'csv',
            'filename': 'supermarket_sales.csv',
            'header': 'true',
            'sep': ','
        })
        
        # Columns
        cols = ET.SubElement(ds, 'columns')
        for field in self.data_spec['fields']:
            col = ET.SubElement(cols, 'column', {
                'name': f'[{field["name"]}]',
                'datatype': 'string' if field['target_type'] == 'string' else 
                           'integer' if field['target_type'] in ['number', 'integer'] else
                           'real' if field['target_type'] == 'float' else
                           'date' if field['target_type'] == 'date' else 'datetime',
                'role': field['role'],
                'type': 'nominal' if field['role'] == 'dimension' else 'quantitative'
            })
        
        # Calculated fields
        for cf in self.data_spec['calculated_fields']:
            col = ET.SubElement(cols, 'column', {
                'name': f'[{cf["name"]}]',
                'datatype': cf['return_type'],
                'role': 'dimension' if cf['return_type'] == 'string' else 'measure',
                'type': 'nominal' if cf['return_type'] == 'string' else 'quantitative',
                'formula': cf['formula']
            })
        
        return ds
    
    def build_worksheet(self, spec):
        ws = ET.Element('worksheet', {'name': spec['name']})
        
        # Table
        table = ET.SubElement(ws, 'table')
        
        # View
        view = ET.SubElement(ws, 'view')
        
        # Panes
        panes = ET.SubElement(view, 'panes')
        pane = ET.SubElement(panes, 'pane', {'selection-relaxation-option': 'selection-relaxation-allow'})
        
        # Mark
        mark = ET.SubElement(pane, 'mark', {'class': spec.get('mark_class', 'Automatic')})
        
        # Encodings
        encodings = ET.SubElement(mark, 'encodings')
        
        # Columns encoding
        cols_enc = ET.SubElement(encodings, 'columns')
        col_enc = ET.SubElement(cols_enc, 'encoding', {
            'field': f'[{spec["columns"]["field"]}]',
            'type': 'quantitative' if spec["columns"].get("aggregation") else 'nominal'
        })
        if spec["columns"].get("aggregation"):
            col_enc.set('aggregation', spec["columns"]["aggregation"])
        if spec["columns"].get("granularity"):
            col_enc.set('granularity', spec["columns"]["granularity"])
        if spec["columns"].get("continuous"):
            col_enc.set('continuous', 'true')
        
        # Rows encoding
        rows_enc = ET.SubElement(encodings, 'rows')
        if isinstance(spec["rows"], list):
            for row_spec in spec["rows"]:
                row_enc = ET.SubElement(rows_enc, 'encoding', {
                    'field': f'[{row_spec["field"]}]',
                    'type': 'quantitative'
                })
                if row_spec.get("aggregation"):
                    row_enc.set('aggregation', row_spec["aggregation"])
                if row_spec.get("format"):
                    row_enc.set('format', row_spec["format"])
        else:
            row_enc = ET.SubElement(rows_enc, 'encoding', {
                'field': f'[{spec["rows"]["field"]}]',
                'type': 'quantitative' if spec["rows"].get("aggregation") else 'nominal'
            })
            if spec["rows"].get("aggregation"):
                row_enc.set('aggregation', spec["rows"]["aggregation"])
        
        # Color encoding. Most sheets use an explicit field. The city
        # comparison spec colors by generated metric names instead.
        if spec.get("color") and spec["color"].get("field"):
            color_enc = ET.SubElement(encodings, 'color')
            color_encoding = ET.SubElement(color_enc, 'encoding', {
                'field': f'[{spec["color"]["field"]}]',
                'type': 'nominal'
            })
            if spec["color"].get("stack"):
                color_encoding.set('stack', 'true')
        elif spec.get("color") and spec["color"].get("by"):
            color_enc = ET.SubElement(encodings, 'color')
            ET.SubElement(color_enc, 'encoding', {
                'field': f'[{spec["color"]["by"]}]',
                'type': 'nominal',
                'generated': 'true'
            })
        
        # Labels
        if spec.get("labels"):
            label_enc = ET.SubElement(encodings, 'label')
            label_encoding = ET.SubElement(label_enc, 'encoding', {
                'field': f'[{spec["labels"]["field"]}]',
                'type': 'quantitative'
            })
            if spec["labels"].get("aggregation"):
                label_encoding.set('aggregation', spec["labels"]["aggregation"])
            if spec["labels"].get("format"):
                label_encoding.set('format', spec["labels"]["format"])
        
        # Filters
        if spec.get("filters"):
            filters = ET.SubElement(ws, 'filters')
            for f in spec["filters"]:
                ET.SubElement(filters, 'filter', {
                    'class': 'categorical',
                    'field': f'[{f}]',
                    'ui': 'dropdown'
                })
        
        # Sort
        if spec.get("sort"):
            sort = ET.SubElement(ws, 'sort', {
                'field': f'[{spec["sort"]["by"]}]',
                'direction': spec["sort"]["order"]
            })
        
        return ws
    
    def build_dashboard(self):
        dash = ET.Element('dashboard', {'name': self.spec['dashboard']['name']})
        
        # Size
        size = ET.SubElement(dash, 'size', {
            'width': str(self.spec['dashboard']['size']['width']),
            'height': str(self.spec['dashboard']['size']['height']),
            'fixed': 'true'
        })
        
        # Zones
        zones = ET.SubElement(dash, 'zones')
        
        # Title zone
        title_zone = ET.SubElement(zones, 'zone', {
            'type': 'title',
            'h': '80',
            'w': '1200',
            'x': '0',
            'y': '0'
        })
        title_text = ET.SubElement(title_zone, 'title')
        title_text.text = self.spec['layout']['title_zone']['text']
        
        # Filter zone
        filter_zone = ET.SubElement(zones, 'zone', {
            'type': 'filter',
            'h': '60',
            'w': '1200',
            'x': '0',
            'y': '80'
        })
        
        # Sheet zones
        y_offset = 140
        row_height = 250
        col_width = 600
        
        for placement in self.spec['layout']['grid']['placements']:
            sheet_name = placement['sheet']
            row = placement['row']
            col = placement.get('col', 0)
            colspan = placement.get('colspan', 1)
            
            x = col * col_width
            y = y_offset + row * row_height
            w = colspan * col_width
            h = row_height
            
            zone = ET.SubElement(zones, 'zone', {
                'type': 'worksheet',
                'name': sheet_name,
                'x': str(x),
                'y': str(y),
                'w': str(w),
                'h': str(h)
            })
        
        # Parameter control zone
        param_zone = ET.SubElement(zones, 'zone', {
            'type': 'parameter-control',
            'parameter': 'Top N Products',
            'x': '20',
            'y': str(140 + len(self.spec['layout']['grid']['placements']) * row_height),
            'w': '200',
            'h': '40'
        })
        
        return dash

def main():
    gen = TWBGenerator()
    xml = gen.build()
    
    output = ROOT / 'luaran' / 'Supermarket_Sales_Dashboard.twb'
    output.parent.mkdir(parents=True, exist_ok=True)
    with open(output, 'w') as f:
        f.write(xml)
    
    print(f"[OK] .twb XML draft generated at {output}")
    print("[NEXT] Open in Tableau Desktop, verify, then File > Export Packaged Workbook (.twbx)")

if __name__ == '__main__':
    main()
