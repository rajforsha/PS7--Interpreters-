from Utils import Utils
class Interpreter:

    def __init__(self):
        self.vertices = [] #list containing languages and interpreter
        self.edges = {} #adjency matrix of edges linking interpreters to languages
        self.interpreters = [] #need to maintain since vertices contain both the langauge and interpreter
        self.utils = Utils()

    def addLanguagesOrInterpreters(self, val):
        val = val.strip()
        if val not in self.vertices:
            self.vertices.append(val)


    def linkInterpretersToLangauages(self, interpreter, language):
        #undirected graph, hence adding to both the ends
        interpreter = interpreter.strip()
        language = language.strip()

        if self.edges.get(interpreter) is None:
            self.edges[interpreter]=[language]
        else:
            self.edges[interpreter].append(language)

        if self.edges.get(language) is None:
            self.edges[language] = [interpreter]
        else:
            self.edges[language].append(interpreter)


    def readInputFile(self, filepath):
        data = self.utils.readFromInputFile(filepath)
        for line in data:
            values = line.strip('\n').split('/')
            name = values[0]
            self.interpreters.append(name.strip())
            self.addLanguagesOrInterpreters(name)
            for i in range(1, len(values)):
                self.linkInterpretersToLangauages(name, values[i])
                self.addLanguagesOrInterpreters(values[i])


    def getAllLanguages(self):
        s1 = set(self.vertices)
        s2 = set(self.interpreters)
        return s1-s2

    def printGraph(self):
        outputResultList = []
        outputResultList.append('--------Function printGraph--------')
        for key,val in self.edges.items():
            outputResultList.append(key +'->'+str(val))

        # write to output file
        self.utils.writeToOutputFile(outputResultList)

    def showAll(self):
        outputResultList = []
        outputResultList.append('--------Function showAll--------')
        outputResultList.append('Total no. of candidates: ' + str(len(self.interpreters)))
        outputResultList.append('Total no. of languages: '+ str(len(self.getAllLanguages())))

        outputResultList.append('List of candidates:')
        for candidate in self.interpreters:
            outputResultList.append(candidate)

        outputResultList.append('List of languages:')

        for language in self.getAllLanguages():
            outputResultList.append(language)

        # write to output file
        self.utils.writeToOutputFile(outputResultList)

    def displayCandidates(self, lang):
        outputResultList = []
        list = self.edges.get(lang)
        outputResultList.append('--------Function displayCandidates--------')
        outputResultList.append('List of Candidates who can speak '+ lang +':')
        for candidate in list:
            outputResultList.append(candidate)

        # write to output file
        self.utils.writeToOutputFile(outputResultList)

    def findDirectTranslator(self, langA, langB):
        outputResultList = []
        outputResultList.append('--------Function findDirectTranslator --------')
        outputResultList.append('LanguageA: '+ langA)
        outputResultList.append('LanguageB: ' + langB)
        candidates = self.edges.get(langA)
        stack = []
        for candidate in candidates:
            stack.append(candidate)

        result = None
        while(len(stack)>0):
            item = stack.pop()
            langauges = self.edges.get(item)
            if(langB in langauges):
                result = candidate
                break

        if(result is None):
            outputResultList.append('Direct Translator: No. ')
        else:
            outputResultList.append('Direct Translator: Yes,'+ result+' can translate.')

        # write to output file
        self.utils.writeToOutputFile(outputResultList)

    def findTransRelation(self, langA, langB):
        outputResultList = []
        outputResultList.append('--------Function findTransRelation --------')
        outputResultList.append('LanguageA: '+ langA)
        outputResultList.append('LanguageB: ' + langB)

        # write to output file
        self.utils.writeToOutputFile(outputResultList)




