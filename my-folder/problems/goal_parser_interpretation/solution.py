class Solution:
    def interpret(self, command: str) -> str:
        dictk = {'G':'G','()':'o','(al)':'al'}
        for k,v in dictk.items():
            command = command.replace(k,v)
            # print(command)
        return command
        