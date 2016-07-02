
"""The original program  does not recognise three or more consecutive Capitalised words as   Named Entities .

Below Modifications made by me aptly handles the scenarios  

Program checks for 2 Named Entities present in the text

1. Los Angeles - Two capitalised words

2. The Hollywood Sign - Three capitalised words


"""



import re
import unittest

"""Declaration of Global Variables word_buffer and temp -which are common for the methods in the program
"""
# Buffer to store current named entity
word_buffer = []

# Global variable to identify the breaks in Named Entities (NE) 
temp =0


# Regular expression for matching a token at the beginning of a sentence
token_re = re.compile(r"([a-z]+)\s*(.*)$", re.I)
# Regular expression to recognize an uppercase token
uppercase_re = re.compile(r"[A-Z][a-z]*$")

def text_token_analyser(text):
	"""
	Take the first token off the beginning of text. If its first letter is
	capitalized, remember it in word buffer - we may have a named entity on our
	hands!!

	@return: Tuple (token, remaining_text). Token is None in case text is empty
	"""
	global word_buffer
	global temp
	token_match = token_re.match(text)
	if token_match:
		token = token_match.group(1)
		if uppercase_re.match(token):
			word_buffer.append(token)

		else:
		   if len(word_buffer)>1: # Helps to identify the break in the Named Entity (eg. Los Angeles last)
		       
		       temp=1
		       
		   else:
		        word_buffer = []
		return token, token_match.group(2)
	return None, text
	
    	
def join_named_entity(words_in_buffer):
        """
	Method to join the entities present in th buffer 
	@ return - Returns the joined Named Entitied eg: ['Hollywood', 'Sign'] will be transformed to "Hollywood Sign"
	"""
    
        joined_entity = " ".join(words_in_buffer)
        
                
        return joined_entity

def check_named_entity(check):
	"""
	Return a named entity, if we have assembled one in the current buffer.
	Returns None if we have to keep searching.
	"""
	global word_buffer
	global temp
	
	
	if check == "All":   
	# @return - Return Named Entities identified from the begining of the sentence except for the Named Entity at the end
  
	  if temp == 1: 
   
		named_entity = join_named_entity(word_buffer)

		word_buffer = []
		
		temp = 0

		return named_entity
	else:
	# @ return - Return Named Entity present at the end of the sentence, if available

	     if len(word_buffer)>1:   
	      
                named_entity = join_named_entity(word_buffer)
                
		return named_entity


class NamedEntityTestCase(unittest.TestCase):

	def test_ner_extraction(self):

		# Remember to change this Unit test as well to follow the interface
		# changes you propose above
		
		text = "When we went to Los Angeles last year we visited The Hollywood Sign"

		entities = set()
		while True:
			token, text = text_token_analyser(text)

			if not token:
			    
			        """ This condition will be satisified only when the token becomes 
			        None which means all the words in the sentence has been processed.
			        """
				entity = check_named_entity("Last") #Calling the method to check if there a NE at the end of sentence
				
				self.assertEqual("The Hollywood Sign", entity) #Test NE at the end of the sentence if returned
				
				
				if entity:
					entities.add(entity)

				break  # End of text - exit from the loop

			entity = check_named_entity("All") #Calling the method to check if there a NE in the sentence except at the end

			if entity:
				entities.add(entity)
		
		self.assertEqual(set(["Los Angeles", "The Hollywood Sign"]), entities) #Test all NE present in the sentence

if __name__ == "__main__":
    unittest.main()