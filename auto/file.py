import os

class File: 
    
    document_dirs = [
        '00_共通管理',
        '10_開発管理',
        '20_技術管理',
        '30_標準管理',
        '40_----------',
        '50_事務管理',
        '60_組織管理',
        '70_人事管理',
        '80_IT管理',
        '90_その他管理',
    ]
    
    work_dirs = [
        'auto',
        'tmp',
        '',
    ] 

    def create_document_dirs(self, dest):

        if not os.path.exists(dest):
            print(f"{dest}")
            os.mkdir(f"{dest}")

        for dir in self.document_dirs:
            print(f"{dest}/{dir}")
            os.mkdir(f"{dest}/{dir}")
            
    def create_work_dirs(self, dest):

        if not os.path.exists(dest):
            print(f"{dest}")
            os.mkdir(f"{dest}")

        for dir in self.work_dirs:
            print(f"{dest}/{dir}")
            os.mkdir(f"{dest}/{dir}")

    def create_20_develop_dirs(self, dest):
        dirs = [
            '00_共通管理',
            '10_進捗管理',
            '20_タスク管理',
            '30_文書管理',
            '40_資産管理',
            '50_納品管理',
            '60_受領管理',
        ]

        for dir in dirs:
            print(f"{dest}/{dir}")
            os.mkdir(f"{dest}/{dir}")    

if __name__ == '__main__':
    file = File()
    file.create_document_dirs(f'F:\\work\\github\\technotes\\auto\\document')
    file.create_work_dirs(f'F:\\work\\github\\technotes\\auto\\work')