#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  solve.py
#  
#  Copyright 2018 Locard <locard@CSC-laptop>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

class xor_solver(object):
	
	def __init__(self, charset_in):
		
		self.charset = charset_in
		self.lookup = self.__make_lookup_hashtable()

	def test(self):

		orig_charset = self.charset[:]

		import string
		
		#1:
		self.__init__(string.printable)
		s = self.solve("a3a9a4a2be81acb7a091aab7aca694b0acbdaab1aca695a4b7a4aea0a0b1b8", 1, is_hex=True)
		#for sol in s:
			#print sol[1]
		assert ("flag{DireToricQuixoticParakeet}" in [sol[1] for sol in s])

		#2:
		self.__init__(string.printable)
		s = self.solve("fd3cebb2e009e5a0f537c6bcef38ef85ee24f8bcff14e5b9eb38e3bbe6", 4, is_hex=True)
		#for sol in s:
		#	print sol[1]
		assert ("flag{YoungLithePutridDolphin}" in [sol[1] for sol in s])

		#Put things back as they were.
		self.__init__(orig_charset)



	def __make_lookup_hashtable(self):

		lookup = {}
		for c1 in self.charset:
			for c2 in self.charset:
				if (c1 != c2):

					key = ord(c1) ^ ord(c2)
					
					v1 = (c1, c2)
					v2 = (c2, c1)
					
					if key not in lookup:
						lookup[key] = set()
					lookup[key].add(v1)
					lookup[key].add(v2)

		return lookup


	#Returns a list of (key, plaintext) pairs.
	def solve(self, rawstr, keylength, is_hex=False):

		if (is_hex):
			str_in = self.hex_to_str(rawstr)
		else:
			str_in = rawstr

		tokens = [str_in[i:(i+keylength)] for i in range(0,len(str_in), keylength)]
		
		keys = []
		
		for k in range(keylength):

			kth_chars = [t[k] for t in tokens if len(t)>k]

			next_key_chars = self.get_key(kth_chars)
			#print next_key_chars

			if (keys):
				new_keys = []
				for ko in keys:
					for kn in next_key_chars:
						new_keys.append(ko+kn)

				keys = new_keys
			else:
				keys = next_key_chars
			
			#print keys
			#raw_input()

		solutions = []
		for k in keys:
			solution = (k, self.decode(str_in, k, assert_valid=True))
			if solution is not None:
				solutions.append(solution)

		return solutions

	def get_key(self, bytes_in):

		graph = self.build_graph(bytes_in)

		H0 = [None] * len(bytes_in)


		self.solutions = []
		self.checkbytes = bytes_in
		self.walk_graph(graph, H0, 0)
		
		things = self.solutions[:]
		
		self.solutions = None
		
		return things

	def build_graph(self, bytes_in):

		edge_lookup = {}

		#Count nodes.
		num_nodes = len(bytes_in)

		#Iterate over edges.
		for el in range(num_nodes):
			for er in range(el+1, num_nodes):

				#This edge.
				e = (el, er)

				#Neighbours.
				L_neighbours_higher = [(el, N) for N in range(el+1, num_nodes) if N!=er]
				L_neighbours_lower  = [(N, el) for N in range(0, el)]

				R_neighbours_higher = [(er, N) for N in range(er+1, num_nodes)]
				R_neighbours_lower  = [(N, er) for N in range(0, er) if N!=el]



				#Get incoming edge possibilities, if we can.
				if (bytes_in[el] == bytes_in[er]):
					continue

				key = ord(bytes_in[el]) ^ ord(bytes_in[er])
				incoming_possibilities = self.lookup[key]

				L_incoming_chars = set([I[0] for I in incoming_possibilities])
				R_incoming_chars = set([I[1] for I in incoming_possibilities])

				#Attempt to reduce these down.


				#Get set of all chars already seen at left node.
				L_seen_chars = set()
				for Ln in L_neighbours_higher:
					if Ln in edge_lookup:
						L_seen_chars.update([E[0] for E in edge_lookup[Ln]])
				for Ln in L_neighbours_lower:
					if Ln in edge_lookup:
						L_seen_chars.update([E[1] for E in edge_lookup[Ln]])


				#Intersection of these two.
				if (len(L_seen_chars) != 0):
					L_valid_chars = L_incoming_chars.intersection(L_seen_chars)
				
					#Throw away any in the incoming set that have now been invalidated.
					incoming_possibilities = set([i for i in incoming_possibilities if i[0] in L_valid_chars])
					
					#Throw away any in neighbouring sets that have now been invalidated.
					for Ln in L_neighbours_higher:
						if Ln in edge_lookup:
							edge_lookup[Ln] = set([i for i in edge_lookup[Ln] if i[0] in L_valid_chars])
					for Ln in L_neighbours_lower:
						if Ln in edge_lookup:
							edge_lookup[Ln] = set([i for i in edge_lookup[Ln] if i[1] in L_valid_chars])
				


				#Get set of all chars already seen at right node.
				R_seen_chars = set()
				for Rn in R_neighbours_higher:
					if Rn in edge_lookup:
						R_seen_chars.update([E[0] for E in edge_lookup[Rn]])
				for Rn in R_neighbours_lower:
					if Rn in edge_lookup:
						R_seen_chars.update([E[1] for E in edge_lookup[Rn]])

				#Intersection of these two.
				if (len(R_seen_chars) != 0):
					R_valid_chars = R_incoming_chars.intersection(R_seen_chars)

					#Throw away any in the incoming set that have now been invalidated.
					incoming_possibilities = set([i for i in incoming_possibilities if i[1] in R_valid_chars])

					#Throw away any in neighbouring sets that have now been invalidated.
					for Rn in R_neighbours_higher:
						if Rn in edge_lookup:
							edge_lookup[Rn] = set([i for i in edge_lookup[Rn] if i[0] in R_valid_chars])
					for Rn in R_neighbours_lower:
						if Rn in edge_lookup:
							edge_lookup[Rn] = set([i for i in edge_lookup[Rn] if i[1] in R_valid_chars])

				#Save.
				edge_lookup[e] = incoming_possibilities

		#Make graph iterable.
		#for e in edge_lookup:
		#	edge_lookup[e] = list(edge_lookup[e])
		return edge_lookup

	def decode(self, s_in, k_in, assert_valid=None):

		keylength = len(k_in)

		plaintext = b""

		for i in range(len(s_in)):

			c = ord(s_in[i]) ^ ord(k_in[i%keylength])
			
			if (assert_valid is not None):
				if (chr(c) not in self.charset):
					return None
			
			plaintext += chr(c)

		return plaintext

	def hex_to_str(self,hexstr_in):
		
		if (len(hexstr_in) % 2 != 0):
			hexstr = "0" + hexstr_in
		else:
			hexstr = hexstr_in

		return b"".join([chr(int(hexstr[i:(i+2)], 16)) for i in range(0, len(hexstr), 2)])

	def walk_graph(self, g, sol, cursor):

		graph_size = len(sol)

		#Stopping condition
		if (cursor == graph_size):
			
			check = [ord(self.checkbytes[i]) ^ ord(sol[i]) for i in range(graph_size)]
			if all([c==check[0] for c in check]):
				#raw_input()
				self.solutions.append(chr(check[0]))

		#Otherwise, proceed.
		else:
			
			#Get all possible chars at this node.
			node_chars = set()
			
			#Left first
			for right in range(cursor+1, graph_size):
				if (cursor, right) in g:
					node_chars.update([I[0] for I in g[(cursor,right)]])
			
			#Then right
			for left in range(cursor):
				if (left, cursor) in g:
					node_chars.update([I[1] for I in g[(left,cursor)]])

			#For each of these chars:
			for c in node_chars:
				
				#Add to solution
				sol[cursor] = c

				#Check that a consistent path can be found
				consistent = True
				for nl in range(graph_size):
					for nr in range(nl+1, graph_size):
						
						if ((sol[nl] is not None) and (sol[nr] is not None)):
							if (nl, nr) in g:
								consistent = consistent and ((sol[nl], sol[nr]) in g[(nl,nr)])
				
				#If it can, step to next node
				if (consistent):
					self.walk_graph(g, sol, cursor+1)

				#If it can't, don't bother stepping to next node
				
				#Remove from solution
				sol[cursor] = None


if __name__ == '__main__':

	myname = __file__

	print """
Here's a sample to get you up and running (I'm trying to guess the filename, so that bit might not be dead accurate):

	from %s import xor_solver
	import string

	x = xor_solver(string.printable)

	solutions = x.solve("fd3cebb2e009e5a0f537c6bcef38ef85ee24f8bcff14e5b9eb38e3bbe6", 4, is_hex=True)

	keys = [s[0] for s in solutions]
	plaintexts = [s[1] for s in solutions]

	assert ("flag{YoungLithePutridDolphin}" in plaintexts)

""" % __file__
