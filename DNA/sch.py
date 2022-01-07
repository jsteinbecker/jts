class weekSchedule:
      def __init__(self,seq):
            self.seq = seq
            self.lst = seq.split(" ")

      def mon (self):
            return self.lst[1]
      def tue (self):
            return self.lst[2]

      def count_workdays (self):
            ct = 7
            for eday in self.lst:
                  if eday == ".":
                        ct = ct - 1
            return ct

wk1 = weekSchedule("7P 7c S . . . .")
wk2 = weekSchedule(". . . . 7c 7P .")

mo1 = [wk1,wk2]

wk1.count_workdays()
wk2.count_workdays()

