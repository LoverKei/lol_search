# summoner data #

class Summoner:
	def __init__(self, name):
		self.inputname = name
	def setSMname(self, name):
		self.SMname = name
	def setSMid(self, userid):
		self.SMid = userid
	def setSMlv(self, userlevel):
		self.SMlv = userlevel
	def setSMtier(self, tier):
		self.SMtier = tier
	def setSMtier(self, tier, tierlv):
		self.SMtier = tier
		self.SMtierlv = tierlv
		