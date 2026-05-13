import json
from lxml import etree
from typing import List, Dict, Any

# This print will run EVERY time this file is imported or run directly
print(f"The value of __name__ is: {__name__}")

def convert_xml_to_json(xml_file: str, 
                       output_json: str,
                       record_types: List[str] = None) -> None:
    """
    Convert Apple Health XML data to JSON format with optional filtering of record types.
    
    Args:
        xml_file (str): Path to the input XML file
        output_json (str): Path where the JSON file will be saved
        record_types (List[str], optional): List of record types to include. If None, includes all.
    """
    # Parse the XML file
    tree = etree.parse(xml_file)
    root = tree.getroot()
    
    # Initialize dictionary to store the data
    health_data = {
        'me': {},
        'export_date': '',
        'runs': [],
        'records': [],
        'activity_summaries': []
    }
    
    # Process each element
    for element in root:
        if element.tag == 'Me':
            health_data['me'] = dict(element.attrib)
        
        elif element.tag == 'ExportDate':
            health_data['export_date'] = element.text
        
        elif element.tag == 'Workout' and element.attrib.get('workoutActivityType') == 'HKWorkoutActivityTypeRunning':
            workout_data = dict(element.attrib)
            # Include any nested metadata
            metadata = []
            for metadata_entry in element:
                if metadata_entry.tag == 'MetadataEntry':
                    metadata.append(dict(metadata_entry.attrib))
            if metadata:
                workout_data['metadata'] = metadata
            health_data['runs'].append(workout_data)
        
        elif element.tag == 'Record':
            # If record_types is specified, only include matching records
            if record_types is None or element.attrib.get('type') in record_types:
                health_data['records'].append(dict(element.attrib))
        
        elif element.tag == 'ActivitySummary':
            health_data['activity_summaries'].append(dict(element.attrib))
    
    # Save to JSON file
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(health_data, f, indent=2)
    
    # Print some statistics
    print(f"Processed data:")
    print(f"- Total runs: {len(health_data['runs'])}")
    print(f"- Total records: {len(health_data['records'])}")
    print(f"- Total activity summaries: {len(health_data['activity_summaries'])}")

# This code only runs when the file is executed directly
if __name__ == "__main__":
    print("This code is running because the file was executed directly")
    
    # Example usage
    # To convert all data:
    # convert_xml_to_json('export.xml', 'health_data_full.json')
    
    # To convert only specific record types:
    selected_types = [
        'HKQuantityTypeIdentifierHeartRate',
        'HKQuantityTypeIdentifierStepCount',
        'HKQuantityTypeIdentifierDistanceWalkingRunning',
        'HKQuantityTypeIdentifierActiveEnergyBurned'
    ]
    convert_xml_to_json('export.xml', 'health_data_filtered.json', record_types=selected_types) 