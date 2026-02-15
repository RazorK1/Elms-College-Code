# NLTK natural language tool kit
# import libraries
import nltk

nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
text = "Machine learning allows machines to learn from data. Natural Language Processing allows machines to understand human languages."

print("Initial text: ", text)
print("*******************************************")

# write your code here
#2
sentences = nltk.sent_tokenize(text)
print("Sentences: ", sentences)
words = nltk.word_tokenize(text)
print("Words: ", words)

#3
bigrams = list(nltk.bigrams(words))
print("Bigrams are",bigrams)
trigrams = list(nltk.trigrams(words))
print("Trigrams are", trigrams)

#4
#Change text2 here
#text2 = "The actor Dwayne Johnson is in Hollywood."

#5
text2 = """Ukraine's President Volodymyr Zelensky thanked his international allies for their support but suggested there were questions remaining over the future security guarantees for his country.

Speaking at the Munich Security Conference in Germany, Zelensky repeatedly thanked American and European allies for helping Ukraine by providing air defense systems that protect infrastructure like power plants and “save lives.”

Previous U.S.-led efforts to find consensus on ending the war, most recently two rounds of talks in Abu Dhabi, the capital of the United Arab Emirates, have failed to resolve difficult issues such as the future of Ukraine’s Donbas industrial heartland that is largely occupied by Russian forces.

Later with reporters, Zelensky questioned how the concept of a free trade zone — proposed by the U.S. — would work in the Donbas region, which Russia insists Kyiv must give up in order to get peace.

He also said that the Americans want peace as quickly as possible and that the U.S. team wants to sign all the agreements on Ukraine at the same time, whereas Ukraine wants guarantees over the country's future security signed first.

European nations, including the U.K. and France, have already said they will commit troops to Ukraine to guarantee its future security. The U.S. is also expected to be involved, and discussions are ongoing about the nature of American support.

Russian officials are opposed to any foreign troop presence in Ukraine, Zelensky suggested, because he says Russian President Vladimir Putin wants to have the opportunity to attack Ukraine again.

Zelensky also said he was surprised that Moscow had replaced the head of its negotiating team before another round of U.S.-brokered talks and suggested the move was a deliberate attempt at delaying negotiations.

During the talks, Russian officials have insisted Ukraine give up more territory in the east of the country to end the war. But Zelensky told the Associated Press that it was “a little bit crazy” to suggest Ukraine withdraw from its own territory or exchange it.

Thousands of Ukrainians have been killed defending the country's Donbas region, he said, noting that 200,000 people live there and it would not be acceptable to effectively hand them over to Russia.

On the concept of a free economic zone, Zelensky expressed skepticism. “Imagine” he said, if foreign soldiers patrolled the zone and Putin provoked them and they left. In that case, he said, there could be a “big occupation” of Ukraine and a lot of losses.

If Putin is given any opportunity for victory, “we don’t know what he will do next,” Zelensky said.

Such a model, Zelensky told the AP, would have “big risks” for Ukraine and for any country that committed to guaranteeing Ukraine's security. But he said he was ready to discuss it as it could be important as a compromise in exchange for securing support to reconstruct Ukraine.

During negotiations, Zelensky said, Moscow has to accept monitoring of a ceasefire and return some 7,000 Ukrainian prisoners of war in exchange for more than 4,000 Russian prisoners held by Ukraine.

Earlier Saturday, drone strikes killed one person in Ukraine and another in Russia, Ukrainian officials said, ahead of fresh talks next week in Geneva aimed at ending the war.

An elderly woman died when a Russian drone hit a residential building in the Black Sea port city of Odesa, Ukraine’s State Emergency Service said.

In Russia, a civilian was killed in a Ukrainian drone strike on a car in the border region of Bryansk, regional Gov. Alexander Bogomaz said.

Russia-installed authorities said a Ukrainian airstrike on a village Saturday wounded 15 people in the Russian-occupied Luhansk region.

The attacks came a day after a Ukrainian missile strike on the Russian border city of Belgorod killed two people and wounded five, according to regional Gov. Vyacheslav Gladkov."""

#Funny misinterpretations:
#ORGANIZATION Munich
#PERSON Kyiv
#ORGANIZATION United Arab Emirates
#PERSON Donbas
#PERSON Ukraine (It says "GPE Ukraine" most of the time)
#PERSON Emergency Service
#PERSON Earlier
#ORGANIZATION Associated (Almost got it)

words2 = nltk.word_tokenize(text2)
POS_tags = nltk.pos_tag(words2)
namedEntities = nltk.ne_chunk(POS_tags)
print(namedEntities)

#Add this code which prints out just the named entities
for chunk in namedEntities: # I forgot to add this part initially. WOOPS!
     if hasattr(chunk, 'label'):
        print(chunk.label(), ' '.join(c[0] for c in chunk))

#6
fdist = nltk.FreqDist(w.lower() for w in words2)
print(fdist.most_common(20))

stopwords = nltk.corpus.stopwords.words('english')
filteredFreqdist = nltk.FreqDist(w.lower() for w in words2 if w.isalnum() and w not in stopwords)
print(filteredFreqdist.most_common(20)) 

#7
# find a word in context in the article
freqword = "president"
print(nltk.Text(words2).concordance(freqword))


#5
#########################################################################################################################################
#News article sample
#https://www.msn.com/en-us/news/world/drone-strikes-kill-2-in-ukraine-and-russia-ahead-of-peace-talks-in-geneva/ar-AA1Wmlp7
'''
Ukraine's President Volodymyr Zelensky thanked his international allies for their support but suggested there were questions remaining over the future security guarantees for his country.

Speaking at the Munich Security Conference in Germany, Zelensky repeatedly thanked American and European allies for helping Ukraine by providing air defense systems that protect infrastructure like power plants and “save lives.”

Previous U.S.-led efforts to find consensus on ending the war, most recently two rounds of talks in Abu Dhabi, the capital of the United Arab Emirates, have failed to resolve difficult issues such as the future of Ukraine’s Donbas industrial heartland that is largely occupied by Russian forces.

Later with reporters, Zelensky questioned how the concept of a free trade zone — proposed by the U.S. — would work in the Donbas region, which Russia insists Kyiv must give up in order to get peace.

He also said that the Americans want peace as quickly as possible and that the U.S. team wants to sign all the agreements on Ukraine at the same time, whereas Ukraine wants guarantees over the country's future security signed first.

European nations, including the U.K. and France, have already said they will commit troops to Ukraine to guarantee its future security. The U.S. is also expected to be involved, and discussions are ongoing about the nature of American support.

Russian officials are opposed to any foreign troop presence in Ukraine, Zelensky suggested, because he says Russian President Vladimir Putin wants to have the opportunity to attack Ukraine again.

Zelensky also said he was surprised that Moscow had replaced the head of its negotiating team before another round of U.S.-brokered talks and suggested the move was a deliberate attempt at delaying negotiations.

During the talks, Russian officials have insisted Ukraine give up more territory in the east of the country to end the war. But Zelensky told the Associated Press that it was “a little bit crazy” to suggest Ukraine withdraw from its own territory or exchange it.

Thousands of Ukrainians have been killed defending the country's Donbas region, he said, noting that 200,000 people live there and it would not be acceptable to effectively hand them over to Russia.

On the concept of a free economic zone, Zelensky expressed skepticism. “Imagine” he said, if foreign soldiers patrolled the zone and Putin provoked them and they left. In that case, he said, there could be a “big occupation” of Ukraine and a lot of losses.

If Putin is given any opportunity for victory, “we don’t know what he will do next,” Zelensky said.

Such a model, Zelensky told the AP, would have “big risks” for Ukraine and for any country that committed to guaranteeing Ukraine's security. But he said he was ready to discuss it as it could be important as a compromise in exchange for securing support to reconstruct Ukraine.

During negotiations, Zelensky said, Moscow has to accept monitoring of a ceasefire and return some 7,000 Ukrainian prisoners of war in exchange for more than 4,000 Russian prisoners held by Ukraine.

Earlier Saturday, drone strikes killed one person in Ukraine and another in Russia, Ukrainian officials said, ahead of fresh talks next week in Geneva aimed at ending the war.

An elderly woman died when a Russian drone hit a residential building in the Black Sea port city of Odesa, Ukraine’s State Emergency Service said.

In Russia, a civilian was killed in a Ukrainian drone strike on a car in the border region of Bryansk, regional Gov. Alexander Bogomaz said.

Russia-installed authorities said a Ukrainian airstrike on a village Saturday wounded 15 people in the Russian-occupied Luhansk region.

The attacks came a day after a Ukrainian missile strike on the Russian border city of Belgorod killed two people and wounded five, according to regional Gov. Vyacheslav Gladkov.
'''
