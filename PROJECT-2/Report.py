# Automated Report Generation

''''
Develop a script that rads data from a file , analyses it, and generates a formatted pdf report using libraries like fpdf or reportlab.
'''

import pandas as pd
from fpdf import FPDF

# Load data
data = pd.read_csv(r"C:\Users\Anupa\Desktop\Tresa Maria\internship\python\PROJECT 2\report.csv")
data.columns = data.columns.str.strip()  # Remove any extra spaces in column names

# Data Analysis
total_employees = len(data)
average_hours = data['Hours_Worked'].mean()
department_counts = data['Department'].value_counts()

# Prepare department-wise summary DataFrame
summary_df = (
    data.groupby('Department')
    .agg(
        Employees=('Name', 'count'),
        Total_Hours=('Hours_Worked', 'sum'),
        Average_Hours=('Hours_Worked', 'mean')
    )
    .reset_index()
)

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Employee Work Hours Report", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def report_summary(self, summary_df):
        self.add_page()
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Department-wise Summary", ln=True)
        self.ln(5)

        # Table headers
        self.set_font("Arial", "B", 11)
        self.set_fill_color(200, 220, 255)
        for header in summary_df.columns:
            self.cell(45, 10, str(header), border=1, fill=True)
        self.ln()

        # Table data
        self.set_font("Arial", "", 11)
        for _, row in summary_df.iterrows():
            self.cell(45, 10, str(row['Department']), border=1)
            self.cell(45, 10, str(row['Employees']), border=1)
            self.cell(45, 10, str(row['Total_Hours']), border=1)
            self.cell(45, 10, f"{row['Average_Hours']:.2f}", border=1)
            self.ln()

    def detailed_table(self, df):
        self.add_page()
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Individual Employee Work Hours", ln=True)
        self.ln(5)

        self.set_font("Arial", "B", 11)
        self.set_fill_color(220, 235, 255)
        self.cell(60, 10, "Name", border=1, fill=True)
        self.cell(60, 10, "Department", border=1, fill=True)
        self.cell(60, 10, "Hours Worked", border=1, fill=True)
        self.ln()

        self.set_font("Arial", "", 11)
        for _, row in df.iterrows():
            self.cell(60, 10, str(row['Name']), border=1)
            self.cell(60, 10, str(row['Department']), border=1)
            self.cell(60, 10, str(row['Hours_Worked']), border=1)
            self.ln()

# Create and Save PDF
pdf = PDF()
pdf.report_summary(summary_df)
pdf.detailed_table(data)
pdf.output("employee_report.pdf")

print("PDF report 'employee_report.pdf' generated successfully.")
