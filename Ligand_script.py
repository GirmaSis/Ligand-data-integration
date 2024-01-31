
import pandas as pd

csv_file_path = 'raw/small library_znd.csv'
data_csv = pd.read_csv(csv_file_path)

excel_file_path = 'raw/109_p10_filtered_datawarrior.xlsx'
data_excel = pd.read_excel(excel_file_path)

data_excel = data_excel.drop(columns=['Structure [idcode]'], errors='ignore')

extracted_values = data_csv['Ligand'].str.extract(r'(ZINC\d+)')[0]

merged_data = pd.merge(
    data_excel,  
    data_csv, 
    left_on='Molecule Name',  
    right_on=extracted_values,
    how='inner'
)

merged_data = merged_data.drop_duplicates(subset=['Molecule Name'])  
merged_data.to_csv('New_py-merged_data.csv', index=False)


merged_data['Extracted_ZINC'] = merged_data['Ligand'].str.extract(r'(ZINC\d+)')[0]
merged_data['Is_Correct_Alignment'] = merged_data['Molecule Name'] == merged_data['Extracted_ZINC']

print(merged_data[['Molecule Name', 'Ligand', 'Extracted_ZINC', 'Is_Correct_Alignment']].head())

merged_data.to_csv('AfterAllignment_New_merged_data.csv', index=False)
print(merged_data['Is_Correct_Alignment'].value_counts())

