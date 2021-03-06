class BaseAgent(object):

    possible_answers = 0
    problem_figures = 0
    problem_name = ""
    problem = None

    def __init__(self, problem):

        self.problem_name = problem.name

        # All problems will need the number of answers to iterate
        if problem.problemType == "2x2":
            self.possible_answers = 6
            self.problem_figures = 3
        else:
            self.possible_answers = 8
            self.problem_figures = 8

        self.problem = problem

    def log(self, messages):
        if __debug__:
            for i in range(0, len(messages)):
                messages[i] = str(messages[i])
            print(" ".join(messages))

    def log_section_header(self, message):
        print("\n***********************************************************************************\n")
        print(message)
        print("\n***********************************************************************************\n")
