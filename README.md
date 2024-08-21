
# Parametric Design Automation

## Overview
**Parametric Design Automation** is a project designed to improve the efficiency of CAD modeling by automating the process of updating model parameters in SolidWorks. By using Python scripts; you can define key parameters in a CSV file, calculate dependent parameters, and update their models in Solidworks with minimal manual effort. 

Because the gear model is relatively simple, I used it for this project.

## Features
- **Automated Parameter Calculation**: Use Python to read a CSV file containing base parameters and formulas, then automatically calculate dependent parameters.


- **Instant Model Updates**: Export the calculated parameters to a .txt file and link it to your SolidWorks model. Use the rebuild button to instantly apply changes.


- **Scalable Design**: Once the base model is created, subsequent models can be quickly generated by modifying the inputs of the python script.

## How It Works
1. **Model Creation**: Start with creating a base model in SolidWorks. Make sure that you use smart dimensioning when building your model so that different dimensions can be linked to the different parameters in the data file.


2. **Define Parameters**: Create a CSV file using Notepad or Excel, listing the key parameters and their formulas.


3. **Run Python Script**: The script reads the CSV file, computes the necessary parameters, and exports the data to a .txt file.


4. **Update Model**: Manually link the .txt file to the SolidWorks model through the formulas section. Click the rebuild button to see the changes reflected in the model.

## Requirements
- SolidWorks
- Python 3.x
- CSV file with defined parameters and formulas
- A little knowledge of Pandas and Numpy

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/Parametric-Design-Automation.git
   ```
2. Ensure you have Python 3.x installed. Install any required Python packages (e.g., `pandas` for CSV handling).
   ```bash
   pip install pandas
   ```
3. Create or modify the CSV file to include your design parameters.


4. Run the Python script to generate the .txt file with updated parameters:
   ```bash
   python Gear.py
   ```
5. Link the generated .txt file to your SolidWorks model through the formulas section.

## Considerations
- **Manual Linking**: This solution requires manual linking of the .txt file to SolidWorks through the formulas section.
- **Base Model Requirement**: A base model must be created initially; subsequent models can be generated from this base.
- **Smart Dimensioning**: Ensure your SolidWorks model has smart dimensioning to allow different parts to be linked to the CSV parameters.
- **CSV Setup**: You'll need to set up a CSV file with the formulas and variables then manually write these formulas in the python script. Optionally, you can extend the script to request user input for these values.

## Example of .CSV file
```csv
Parameter, Formula, Comment
P,2,Diametral Pitch
N,18,Number of teeth
phi,20,Pressure angle
a,1/P,Addendum
b,1.25/P,Dedendum
```
The python script requires user input for independent parameters so any value can be used for them when creating the .csv file

## Contributing
Feel free to fork this project, submit pull requests, or raise issues if you find bugs or have suggestions for improvements.

## Contact
For any questions or inquiries, please contact me through [LinkedIn](https://www.linkedin.com/in/victor-agbaso) or open an issue on this repository.