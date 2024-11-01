- Prompt 1
  you are a python expert.
  create multiple choice exercises about recursion in python separated by 3 quotes.
  multiple choice exercises for 2nd year information technology students.
  '''Recursion Python also accepts function recursion, which means a defined function can call itself.
  Recursion is a common mathematical and programming concept.
  It means that a function calls itself.
  This has the benefit of meaning that you can loop through data to reach a result.
  The developer should be very careful with recursion as it can be quite easy to slip into writing a function that never terminates, or one that uses excess amounts of memory or processor power.
  However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
  In this example, tri_recursion() is a function that we have defined to call itself ("recurse").
  We use the k variable as the data, which decrements (-1) every time we recurse.
  The recursion ends when the condition is not greater than 0 (i.
  e.
  when it is 0).
  To a new developer it can take some time to work out how exactly this works, the best way to find out is by testing and modifying it.
  '' '.
  The multiple choice exercise has about 10 questions.
  First, create questions about the theory in the passage.
  Then, give questions about applying and guessing the results in the console.
  Finally, 2 high application questions.
- Prompt 2
  You are a writer.
  Analyze and write more paragraphs separated by <>.
  <Recursion is particularly efficient when working with hierarchical data structures like trees.
  In a file system, for instance, each folder may contain subfolders and files, which can be processed recursively.
  A recursive function can traverse the file system by iterating through each item and making recursive calls to explore subdirectories.
  The elegant nature of recursion allows developers to write compact and intuitive code to handle such complex data structures effortlessly.
  > Then give specific examples of recursion.
  > Give patterns that developers often use.
  > If possible, make them humorous.
  > And show why people use recursion in that case.
- Prompt 3
  Phân loại thành review tốt và xấu,lấy thêm các bài đánh giá ở trên google map , tổng hợp và đếm số review tại địa điểm The Coffee House - Bình Phú.
  đánh giá tích cực là đánh giá từ 4 đến 5 sao.
  còn tiêu cực là đánh giá dưới 4 sao.
  phỏng đoán liệu họ có đến quán hay không dựa trên bình luận và đưa ra giải pháp cho từng bình luận và đưa ra giải pháp chung cho quán để tăng sự hài lòng của khách.
  mỗi đánh giá tích cực và tiêu hãy đưa khoảng 10 ví dụ với format là.
  name :.
  đánh giá :.
  số sao mà họ đánh giá :.
  phỏng đoán :
- Prompt 4
  debug The following code
  <
  def docx_to_txt(file_docx, file_txt):
  docx = Document(file_docx)
  with open(file_txt, "w", encoding="utf-8") as file:
  for line in docx.file:
  file.write(line.text + "\n")
  >
- improve it to make it easier to read in file.txt.
- explain each line of the above code to me who knows nothing about the python-docx library.
- provide more information about the library.
- give 10 commonly used commands in the library that developers often use. For each of the 10 commands, explain clearly and give example code for which case it is used

- Prompt 5
  you are a tour guide.
  please guide me when i go to da nang in vietnam.
  but i only have about 1 million vnd.
  introduce the attractions, activities, famous food, visiting time, hotel that is affordable for 2 days trip.
  and gas money i go from ho chi minh city to da nang.
  please plan for me with the following format:.
  day 1:.
  -what time do what:.
  -where and how much.
  -address on google maps.
  -travel cost to the location:.
  day 2:.
  -what time do what:.
  -where and how much.
  -address on google maps.
  -travel cost to the location:
- Prompt 6
  Summarize the plot of the book "The Shining" by Stephen King and list the characters that appear.
  Give good and bad ratings, based on the principle.
  Good characters will help the main character without taking advantage of themselves.
  Bad characters will hinder the main character from completing the mission.
  List additional supporting characters that help deepen the plot.
  Give 10 of each good and bad character.
  And list the supporting characters separately.
  Then summarize for me the content of the novel and the awards it has received.
  Which chapter in the novel is the most popular according to a reputable rating organization?.
