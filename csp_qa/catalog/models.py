from django.db import models
from django.urls import reverse #Used to generate URLS by reversing the URL pattern

class TF_Question(models.Model):
    '''a True/False question'''
    assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE)
    question = models.TextField()
    original = models.BooleanField(verbose_name='Is Original Question?', default=True, help_text="check means yes")
    c = (('T','True'),('F','False'))
    response = models.CharField(max_length=1,choices=c,verbose_name='Correct response',default='T')

    def __str__(self):
        return f'TF: {self.question[:25]}'

class SA_Question(models.Model):
    '''a Short Answer question'''
    assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE)
    question = models.TextField()
    original = models.BooleanField(verbose_name='Is Original Question?', default=True, help_text="check means yes")
    response = models.CharField(max_length=200,verbose_name='Correct response')

    def __str__(self):
        return f'SA: {self.question[:25]}'

class MC_Question(models.Model):
    '''a Multiple Choice question'''
    assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE)
    question = models.TextField()
    original = models.BooleanField(verbose_name='Is Original Question?', default=True, help_text="check means yes")
    c = models.CharField(max_length=200,verbose_name='Correct choice')
    r1 = models.CharField(max_length=200,verbose_name='Wrong choice')
    r2 = models.CharField(max_length=200,verbose_name='Wrong choice')
    r3 = models.CharField(max_length=200,verbose_name='Wrong choice')

    def __str__(self):
        return f'MC: {self.question[:25]}'

class FB_Question(models.Model):
    '''a Fill in the Blank question'''
    assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE)
    question = models.TextField(verbose_name='Question',help_text='use a single underscore "_" to mark a blank')
    original = models.BooleanField(verbose_name='Is Original Question?', default=True, help_text="check means yes")
    blanks = models.CharField(max_length=200,help_text='use semi-colons ";" to seperate blanks')
    num_blanks = models.PositiveSmallIntegerField(verbose_name='How many blanks?',help_text='this helps me catch errors')

    def __str__(self):
        return f'FB: {self.question[:25]}'

class Assignment(models.Model):
    '''an Assignment with 10 questions'''
    NAMES = (
    ('1','1: Early Computing'),
    ('2','2: Electronic Computing'),
    ('3','3: Boolean Logic & Logic Gates'),
    ('4','4: Representing Numbers and Letters with Binary'),
    ('5','5: How Computers Calculate - the ALU'),
    ('6','6: Registers and RAM'),
    ('7','7: The Central Processing Unit (CPU)'),
    ('8','8: Instructions & Programs'),
    ('9','9: Advanced CPU Designs'),
    ('10','10: Early Programming'),
    ('11','11: The First Programming Languages'),
    ('12','12: Programming Basics: Statements & Functions'),
    ('13','13: Intro to Algorithms'),
    ('14','14: Data Structures'),
    ('15','15: Alan Turing'),
    ('16','16: Software Engineering'),
    ('17','17: Integrated Circuits & Moore\'s Law'),
    ('18','18: Operating Systems'),
    ('19','19: Memory & Storage'),
    ('20','20: Files & File Systems'),
    ('21','21: Compression'),
    ('22','22: Keyboards & Command Line Interfaces'),
    ('23','23: Screens & 2D Graphics'),
    ('24','24: The Cold War and Consumerism'),
    ('25','25: The Personal Computer Revolution'),
    ('26','26: Graphical User Interfaces'),
    ('27','27: 3D Graphics'),
    ('28','28: Computer Networks'),
    ('29','29: The Internet'),
    ('30','30: The World Wide Web'),
    ('31','31: Cybersecurity'),
    ('32','32: Hackers & Cyber Attacks'),
    ('33','33: Cryptography'),
    ('34','34: Machine Learning & Artificial Intelligence'),
    ('35','35: Computer Vision'),
    ('36','36: Natural Language Processing'),
    ('37','37: Robots'),
    ('38','38: Psychology of Computing'),
    ('39','39: Educational Technology'),
    ('40','40: The Singularity, Skynet, and the Future of Computing'),
    )
    name = models.CharField(max_length=2, verbose_name='Assignment Name',choices=NAMES)

    def __str__(self):
        return self.name
