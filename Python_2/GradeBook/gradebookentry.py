
class GradebookEntry:
    def __init__(self):
        self._scores = {}

    def add_midterm_exam_score(self, score):
        if 'midterm' not in self._scores:
            self._scores['midterm'] = []
        self._scores['midterm'].append(score)

    def add_project_score(self, score):
        if 'project' not in self._scores:
            self._scores['project'] = []
        self._scores['project'].append(score)

    def add_final_exam_score(self, score):
        self._scores['final'] = score

    def get_midterm_exam_scores(self):
        return self._scores['midterm']

    def get_project_scores(self):
        return self._scores['project']

    def get_final_exam_score(self):
        return self._scores['final']

class GradebookEntryDropLowestProject(GradebookEntry):
    def __init__(self):
        super().__init__()

    def get_project_scores(self):
        return sorted(self._scores['project'])[1:]

class GradebookEntryDropLowestMidterm(GradebookEntry):
    def __init__(self):
        super().__init__()

    def get_midterm_exam_scores(self):
        return sorted(self._scores['midterm'])[1:]

def main():
    ge = GradebookEntry()
    ge.add_project_score(90)
    ge.add_project_score(30)
    ge.add_project_score(50)
    print(ge.get_project_scores())
    ge.add_midterm_exam_score(50)
    ge.add_midterm_exam_score(90)
    ge.add_midterm_exam_score(70)
    print(ge.get_midterm_exam_scores())

    gb = GradebookEntryDropLowestProject()
    gb.add_project_score(90)
    gb.add_project_score(30)
    gb.add_project_score(50)
    print(gb.get_project_scores())

    gh = GradebookEntryDropLowestMidterm()
    gh.add_midterm_exam_score(50)
    gh.add_midterm_exam_score(90)
    gh.add_midterm_exam_score(70)
    print(gh.get_midterm_exam_scores())
main()

