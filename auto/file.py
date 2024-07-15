import os

class File: 
    
    document_top_dir = f"F:\\work\\github\\technotes\\auto\\document"
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
    
    work_top_dir = f'F:\\work\\github\\technotes\\auto\\work'
    work_dirs = [
        'auto',
        'develop',
        'tech',
        'tmp',
        '',
    ] 

    def create_document_dirs(self):

        if not os.path.exists(self.document_top_dir):
            print(f"{self.document_top_dir}")
            os.mkdir(f"{self.document_top_dir}")

        for dir in self.document_dirs:
            print(f"{self.document_top_dir}/{dir}")
            os.mkdir(f"{self.document_top_dir}/{dir}")
            
    def create_work_dirs(self):

        if not os.path.exists(self.work_top_dir):
            print(f"{self.work_top_dir}")
            os.mkdir(f"{self.work_top_dir}")

        for dir in self.work_dirs:
            print(f"{self.work_top_dir}/{dir}")
            os.mkdir(f"{self.work_top_dir}/{dir}")

    def create_20_develop_dirs(self):
        dirs = [
            '00_共通管理',
            '10_進捗管理',
            '20_タスク管理',
            '30_文書管理',
            '40_資産管理',
            '50_納品管理',
            '60_受領管理',
        ]

if __name__ == '__main__':
    file = File()
    file.create_document_dirs()
    file.create_work_dirs()