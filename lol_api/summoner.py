# summoner data #

class Summoner:
# u_name
# u_id
# u_lv
# u_tier
# u_leagueName
# u_division
# u_leaguePoints
# u_wins
# u_lossed
# u_status : 
#	200 - Ranked / 201 - UnRanked
#	0   - Can not find user_info in DB
#   others - RIOT API response.status_code

	def __init__(self, name):
		self.u_name = name
	
	def setUname(self, name):
		self.u_name = name
	def getUname(self):
		return self.u_name

	def setUid(self, userid):
		self.u_id = userid
	def getUid(self):
		return self.u_id

	def setUlv(self, userlevel):
		self.u_lv = userlevel
	def getUlv(self):
		return self.u_lv

	def setUtier(self, tier):
		self.u_tier = tier
	def getUtier(self):
		return self.u_tier

	def setUleagueName(self, leagueName):
		self.u_leagueName = leagueName
	def getUleagueName(self):
		return self.u_leagueName

	def setUdivision(self, division):
		self.u_division = division
	def getUdivision(self):
		return self.u_division

	def setUleaguePoints(self, leaguePoints):
		self.u_leaguePoints = leaguePoints
	def getUleaguePoints(self):
		return self.u_leaguePoints

	def setUwins(self, wins):
		self.u_wins = wins
	def getUwins(self):
		return self.u_wins

	def setUlossed(self, lossed):
		self.u_lossed = lossed
	def getUlossed(self):
		return self.u_lossed

	def setUstatus(self, status):
		self.status = status
	def getUstatus(self):
		return self.status
