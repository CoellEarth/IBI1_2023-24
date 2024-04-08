class students:
    def __init__(self, name, major, code_portfolio_score, group_project_score, exam_score):
        self.name = name 
        self.major = major
        self.code_portfolio_score = code_portfolio_score
        self.group_project_score = group_project_score
        self.exam_score = exam_score
    
    def all_information(self):
        return f"Student {self.name} whose major is {self.major} gained {self.code_portfolio_score} in the ICA of code portfolio, {self.group_project_score} in the ICA of group project, and {self.exam_score} in the final."

# Example usage:
student1 = students("John Doe", "BMI", 85, 90, 75)
print(student1.all_information())
#output:Student John Doe whose major is BMI gained 85 in the ICA of code portfolio, 90 in the ICA of group project, and 75 in the final.
