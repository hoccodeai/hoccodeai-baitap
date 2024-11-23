- Prompt 1
  As a teching assistance, make a list of multiple choice question has at least 10 questions about a lesson. The lesson has content delimited by quote:
  "
  [Lesson Content]
  "
- Prompt 2
  I have a short paragraph, analyze the meaning of the paragraph in the double quotes
  ""
  The character's true given name is never revealed to the reader. After having run away from home, he chooses the new name "Kafka", in honor of writer Franz Kafka. Kafka is described as being muscular for his age and a "cool, tall, fifteen-year-old boy lugging a backpack and a bunch of obsessions". He's also the son of the famous sculptor Koichi Tamura. His mother and sister left the family when he was four years old and he can't remember their faces. He occasionally interacts with his metaphysical alter ego "The boy named Crow" ("Kafka" sounds like "kavka", which means "jackdaw", a crow-like bird, in Czech). Crow tells Kafka throughout the novel that he must be "the toughest fifteen-year-old in the world" and thus motivates him to pursue the journey of running away from home. It is heavily suggested throughout the novel that he, Miss Saeki, and Nakata are somehow connected by an 'alternate reality' on which metaphysical objects from people's subconsciousness take form leading them to find an 'essence' to their lives in exchange for taking away a 'part' of their soul.
  ""
- Prompt 3
  Review 1: "The restaurant is very good, i really like this, i will come back again." => positive review
  Review 2: "very terrible, everything is bad, food has bad smell, it is the last time i come to this restaurant." => negative review
  From a list reviews, please categorize the review in the list into positive and negative and count the total number of comments.
  [
  "I really love Korean noodles, and I feel satisfied cooking here in a Korean metal pot.",
  "Personally, the rich sauce is suitable for dipping bread, a mixed pan of beef, eggs, sausage, shumai,... is quite filling, so you should also consider it when your appetite is weak."
  "Too bad!!!!!!
  - Extremely unpleasant service attitude
  - The owner's attitude is exactly the same as the waitress's
    "Preparing the order took EXTREMELY LONG time, from the time I got a table (not counting the time waiting for the table) to the time the food arrived was 32 minutes - too bad."
    "
    The restaurant is airy
    The owner is enthusiastic and very cute
    Delicious food, rich flavor, reasonable price
    "
    ]
- Prompt 4
  You will be provided a piece of code, your task is finding bugs, explain it in a concise way.
  "
  const getCountryByCountryCode = (countryCode?: string | null) => {
  if (!countryCode) {
  return {
  code: '',
  label: '',
  phone: '',
  };
  }
  const country = find(COUNTRIES, (o) => upperCase(o.code) === upperCase(countryCode));

  if (!country) {
  return {
  code: '',
  label: '',
  phone: '',
  };
  }

  return country;
  };
  ""

- Prompt 5
    You are a tour guide, Introduce about Ho CHi Minh city, list some famous places we have to go when we travel in HCMC
- Prompt 6
    Make a brief about a famous book "The Great Gatsby", then make a list of characters in the novel.