from sploitkit import *


class initacc(Command):
    """ Initial access """
    level = "module"
    single_arg = True

    def complete_values(self):
        #TODO: compute the list of possible values
        return []

    def run(self):
        #TODO: compute results here
        pass

    def validate(self, value):
        #TODO: validate the input value
        if value not in self.complete_values():
            raise ValueError("invalid value")


class Show(Command):
    """ Show options, projects, modules or issues (if any) """
    level = "module"
    single_arg = True
    keys = ["TacticalObjectives","Initial Access", "Execution", "Persistence","Privilege Escalation","Defense Evasion","Credential Access","Discovery","Lateral Movement","Collection","Command and Control","Exfiltration","Impact"]
    
    def complete_values(self, key):
        obj = ["Initial Access", "Execution", "Persistence","Privilege Escalation","Defense Evasion","Credential Access","Discovery","Lateral Movement","Collection","Command and Control","Exfiltration","Impact"]
        
        if key == "TacticalObjectives":
            for i in range(len(obj)):
                print(obj[i])
        elif key == "options":
            return list(self.config.keys())
        elif key == "projects":
            return projects(self)
        elif key == "issues":
            l = []
            for cls, subcls, errors in Entity.issues():
                l.extend(list(errors.keys()))
            return l
    
    def run(self, key, value=None):
        if key == "modules":
            h = Module.get_help(value)
            if h.strip() != "":
                print_formatted_text(h)
            else:
                self.logger.warning("No module loaded")
        elif key == "options":
            if value is None:
                print_formatted_text(ANSI(str(self.config)))
            else:
                c = Config()
                c[self.config.option(value)] = self.config[value]
                print_formatted_text(ANSI(str(c)))
        elif key == "projects":
            if value is None:
                data = [["Name"]]
                for p in projects(self):
                    data.append([p])
                print_formatted_text(BorderlessTable(data, "Existing projects"))
            else:
                print_formatted_text(value)
        elif key == "issues":
            t = Entity.get_issues()
            if len(t) > 0:
                print_formatted_text(t)
    
    def set_keys(self):
        if Entity.has_issues():
            self.keys += ["issues"]
        else:
            while "issues" in self.keys:
                self.keys.remove("issues")

class run(Command):
    level="module"

    def run(self):
        print("running...")


class CommandWithTwoArgs(Command):
    """ Description here """
    level = "module"

    def complete_keys(self):
        #TODO: compute the list of possible keys
        return []

    def complete_values(self, key=None):
        #TODO: compute the list of possible values taking the key into account
        return []

    def run(self):
        #TODO: compute results here
        pass