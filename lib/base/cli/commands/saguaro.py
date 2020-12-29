from sploitkit import *
import smtplib

# For guessing MIME type
import mimetypes

# Import the email modules we'll need
import email
import email.mime
import email.mime.application
from email.mime import multipart
from email.mime import text
from email.mime.multipart import MIMEMultipart

class IA(Command):
    """ Initial access """
    level = "module"
    single_arg = True
    #keys = ["Initial Access","Persistence","Credential Access","Command and Control"]

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
    keys = ["Initial Access","Persistence","Credential Access","Command and Control"]
    def complete_values(self, key):
        obj = ["Initial Access","Persistence","Credential Access","Command and Control"]
        IA = ["Spearphishing Attachment"]
        P = ['Registry Run Keys']
        CA = ['Steal Web Session Cookie']
        C2 = ['Multi-Stage Channels']
        
        if key == "Initial Access":
            print(IA)
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
        # Import smtplib for the actual sending function

        # Create a text/plain message
        msg = email.mime.multipart.MIMEMultipart()
        msg['Subject'] = 'Nuevo programa de sueldos 2021.'
        msg['From'] = 'wwhite@ecorp.local'
        msg['To'] = 'Administrator@ecorp.local'

        # The main body is just another attachment
        body = email.mime.text.MIMEText("""Estimados empleados de ecorp, les hago saber en el siguiente documento sobre los cambios que tendremos en las nómina​s y los sueldos para el año entrante.
        Saludos, y excelente fin de año!
        Walter White
        Director General
        """)
        msg.attach(body)

        # Attach PDF 
        filename='plan2021.pdf'
        fp=open(filename,'rb')
        att = email.mime.application.MIMEApplication(fp.read(),_subtype="pdf")
        fp.close()
        att.add_header('Content-Disposition','attachment',filename=filename)
        msg.attach(att)


        #Attach JS

        #filename='attachments/test.js'
        #fp=open(filename,'rb')
        #att = email.mime.application.MIMEApplication(fp.read(),_subtype="js")
        #fp.close()
        #att.add_header('Content-Disposition','attachment',filename=filename)
        #msg.attach(att)

        # send via Gmail server
        # NOTE: my ISP, Centurylink, seems to be automatically rewriting
        # port 25 packets to be port 587 and it is trashing port 587 packets.
        # So, I use the default port 25, but I authenticate. 
        s = smtplib.SMTP(host='ecorp.local')
        #s.starttls()
        #s.login('xyz@gmail.com','xyzpassword')
        s.sendmail('wwhite@ecorp.local',['Administrator@ecorp.local'], msg.as_string())
        msg['To'] = 'sjohnson@ecorp.local'
        s.sendmail('wwhite@ecorp.local',['sjhonson@ecorp.local'], msg.as_string())
        msg['To'] = 'ajepsen@ecorp.local'        
        s.sendmail('wwhite@ecorp.local',['ajepsen@ecorp.local'], msg.as_string())
        msg['To'] = 'wanderson@ecorp.local'
        s.sendmail('wwhite@ecorp.local',['wanderson@ecorp.local'], msg.as_string())
        s.quit()


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
