### Ligand binding data synthesis: Integrating physicochemical and affinity metrics

It focuses on merging and analyzing datasets to extract meaningful insights, specifically related to ligand efficiency and binding affinity. <br>

The project utilizes data from two primary sources found in the /raw/ folder:
1. ***small library_znd.csv*** containing ligands with their respective binding affinity values.
2. ***109_p10_filtered_datawarrior.xlsx*** generated from the Data Warrior tool, providing detailed physicochemical parameters.

***Goal:*** to integrate these datasets to create a unified view that combines binding affinity data with physicochemical properties. This integration is pivotal for further analysis in drug discovery and molecular docking studies.

**Steps followed:** <br>
***Data Extraction and Cleaning:*** 
Implementing Python and pandas to extract specific 'ZINC' codes from ligand names and cleaning the datasets for precise analysis.

***Data Alignment and Verification:*** 
Aligning the 'ZINC' codes from the CSV file with 'Molecule Names' in the Excel file. This step ensures that the datasets correspond accurately to each other for valid comparisons.

***Dataframe Merging:***
Utilizing pandas to merge dataframes based on common identifiers, ensuring that each 'Molecule Name' has a unique and corresponding ligand and binding affinity data.

***Data Integrity Checks:***
Conducting thorough checks to confirm the correctness of the merged data, ensuring accurate alignment of 'Molecule Names' with the extracted 'ZINC' codes.

***Resultant Data Analysis:*** 
The merged dataset facilitates comprehensive analysis, enabling insights into the relationship between molecular structures and their binding affinities, a key aspect in the evaluation of potential drug candidates.
