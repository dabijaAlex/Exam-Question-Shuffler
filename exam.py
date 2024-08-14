import random
import os
from docx import Document


class Create_All_files():
    
    @staticmethod
    def take_input_from_file(path):
        exercitii = []
        f = open(path, "r")
        numbers = "0123456789"
        index_exercitii = -1

        for x in f:
            if x[0] in numbers:
                exercitii.append(x)
                index_exercitii += 1
                exercitii[index_exercitii] = "\t" + exercitii[index_exercitii]
            else:
                exercitii[index_exercitii] += "\t"
                exercitii[index_exercitii] += str(x)

        random.shuffle(exercitii)

        return exercitii

    @staticmethod
    def create_Dir(parent_dir):

        directory = "SubiecteWord"
        
        # Parent Directory path 
        # parent_dir = "."
        
        # Path 
        path = os.path.join(parent_dir, directory) 
        
        try:
            os.mkdir(path) 
        except FileExistsError:
            a = 1

    @staticmethod
    def init_WordDocs(path_to_folder):
        fisiere = []
        for i in range(1, 15):
            file_name = (f"{path_to_folder}/SubiecteWord/SubiectNr{i}.docx")
            fisiere.append(file_name)
            document = Document('test.docx')
            document.save(file_name)
        return fisiere

    @staticmethod
    def cat_questions(fisiere, exercitii):

        contor = 0
        nr_file = 0
        document = Document(fisiere[nr_file])
        for x in exercitii:
            p = document.add_paragraph(style='List Number')
            run = p.add_run(x)
            run.bold = True
            contor += 1
            if contor == 9:
                document.save(fisiere[nr_file])
                nr_file += 1
                document = Document(fisiere[nr_file])
                contor = 0

    @staticmethod
    def exec_all(path_to_folder):
        path = "test.in"
        Create_All_files.create_Dir(path_to_folder)
        exercitii = Create_All_files.take_input_from_file(path)
        fisiere = Create_All_files.init_WordDocs(path_to_folder)
        Create_All_files.cat_questions(fisiere, exercitii)
