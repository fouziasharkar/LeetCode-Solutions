import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:

    df1 = students.merge(subjects,how='cross')

    #attended_exam
    df2 = examinations.groupby(['student_id','subject_name']).agg(

        attended_exams = ('subject_name','count') 

    ).reset_index()

    df3 = df1.merge(df2, on=['student_id','subject_name'], how='left').sort_values(by=['student_id','subject_name'])

    df3['attended_exams'] = df3['attended_exams'].fillna(0)


    return df3

    

