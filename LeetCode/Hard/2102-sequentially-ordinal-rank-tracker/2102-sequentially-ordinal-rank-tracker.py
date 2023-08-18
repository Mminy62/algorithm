from sortedcontainers import SortedList
class SORTracker:

	def __init__(self):
		self.cnt = 0
		self.lst = SortedList()

	def add(self, name: str, score: int) -> None:
		self.lst.add((-score,name))

	def get(self) -> str:
		self.cnt+=1
		return self.lst[self.cnt-1][1]