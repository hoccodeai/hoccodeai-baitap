## Prompt 1
You're a professor of AI. Make 10 multiple choice questions for beginner depend on the text delimited by triple quotes

Format: 
Question 1: What is CNN?
A. [answer1]
B. [answer2]
C. [answer3]
D. [answer4]
[true answer] - [where on the text tell the true]
"""A convolutional neural network (CNN) is a category of machine learning model. Specifically, it is a type of deep learning algorithm that is well suited to analyzing visual data. CNNs are commonly used to process image and video tasks. And, because CNNs are so effective at identifying objects, they are frequently used for computer vision tasks, such as image recognition and object recognition, with common use cases including self-driving cars, facial recognition and medical image analysis. 

Older forms of neural networks often needed to process visual data in a gradual, piece-by-piece manner -- using segmented or lower-resolution input images. A CNN's comprehensive approach to image recognition enables it to outperform a traditional neural network on a range of image-related tasks and, to a lesser extent, speech and audio processing.

CNN architecture is inspired by the connectivity patterns of the human brain -- in particular, the visual cortex, which plays an essential role in perceiving and processing visual stimuli. The artificial neurons in a CNN are arranged to efficiently interpret visual information, enabling these models to process entire images.

CNNs also use principles from linear algebra, particularly convolution operations, to extract features and identify patterns within images. Although CNNs are predominantly used to process images, they can also be adapted to work with audio and other signal data."""
## Prompt 2
You're literary writer. Make the paragraph analysis by a list on the text delimited by triple quotes. 
Format: 
[summarize all of story]
[list of all character in the text]: [role of character in the text]
-----------------------
Paragraph 1 [word start of paragraph] ... [word end of paragraph]
[main purpose of paragraph]
[scene in paragraph] 
[character in paragraph] : [action character]
-----------------------
[Meaning of story] : [What can we learn?]
 


"""Once upon a time, in a charming English countryside, there lived a curious young girl named Alice. One sunny afternoon, Alice was sitting by a riverbank, feeling a little bored. She glanced up and noticed a white rabbit with pink eyes, dressed in a vest, hurrying by. The rabbit pulled out a pocket watch, saying loudly, “Oh dear! Oh dear! I shall be late!”

Very interested, Alice jumped up and followed the rabbit. She watched as he disappeared into a large rabbit hole. Without thinking twice, Alice followed him down the hole and found herself falling down, down, down into a strange and wonderful world.

Alice landed softly in a hallway filled with doors of all sizes. On a glass table, she found a small golden key and a bottle labeled “Drink Me.” She sipped the potion and began to shrink until she was just the right size to fit through a tiny door that led to a beautiful garden.

As Alice explored Wonderland, she met many strange characters. First, she encountered a talking Caterpillar sitting on a mushroom. He gave her confusing advice and told her that the mushroom could change her size. Alice took a piece of the mushroom and continued on her journey.

Next, she met the Cheshire Cat, a grinning cat who could appear and disappear whenever he wanted. The Cheshire Cat told Alice to go to the March Hare’s house, where she found the Mad Hatter and the Dormouse having a never-ending tea party. The Mad Hatter and the March Hare were quite silly indeed, constantly switching seats and talking in riddles. Alice found their actions amusing but also a bit frustrating.

After leaving the tea party, Alice wandered into the garden of the Queen of Hearts. The Queen was a bossy ruler who loved to play croquet with flamingos as hammers and hedgehogs as balls. The Queen was quick to anger, frequently shouting, “Off with their heads!” whenever she was displeased. Despite the Queen’s scary demeanor, Alice bravely stood up to her.

During the game, Alice met the King of Hearts and the royal court, including a variety of living playing cards. The Queen said that the Knave of Hearts had stolen her tarts, and a meeting was held to decide if he was guilty. The court events were silly and chaotic, with witnesses like the Mad Hatter and the March Hare giving stories that didn’t make sense.

As the trial grew more ridiculous, Alice found herself growing larger and larger. The Queen demanded her execution, but Alice, now towering over everyone, simply declared, “You’re nothing but a pack of cards!” At that moment, the entire court rose into the air and came tumbling down upon her.

Suddenly, Alice woke up on the riverbank, back in the real world. She realized that her adventures in Wonderland had been a dream. She looked around and saw her sister still reading a book nearby.

Alice smiled and thought about all the curious and wonderful characters she had met in her dream. Though it had all been an amazing and unreal adventure, Alice knew she would always remember her journey through Wonderland and the lessons she learned about curiosity, bravery, and standing up for herself."""
## Prompt 3
Input: "list of reviews"

Output: For each review in the list, classify it as "good" or "bad" based on sentiment. Also, determine if the review is "synthetic" (i.e., neutral or generic) or "real" (i.e., has clear sentiment). Finally, return the total count of reviews in the list. Replay "OK" if you ready 

Format:
- For each review, output: "Review: [review], Review Type: [good/bad], Synthetic: [yes/no]"
- At the end, provide: "Review count: [number of reviews]"

"This product is amazing, I love it!"
"Terrible experience, will never buy again."
"It's okay, but not what I expected."
"The quality is fantastic, worth every penny!"
"Not great, I expected more from this brand."
"Absolutely terrible! I want a refund."
"Really good value for the price, I'm happy with my purchase."
"This product is just average, nothing special."
"I’m so disappointed with this, it broke after a week."
"Great purchase, exceeded my expectations!"

## Prompt 4
You're senior python developer. Provide a detailed comment explaining the code and suggest any changes to improve it according to best practices.

!pip install opencv-python

import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive')
image_path = '/content/drive/MyDrive/cavang.jpg'
image = cv2.imread(image_path)
image = cv2.resize(image, (500, 500))
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
mask = np.zeros(image_rgb.shape[:2], np.uint8)

bgd_model = np.zeros((1, 65), np.float64)
fgd_model = np.zeros((1, 65), np.float64)
rect = (50, 50,0 , 0)
cv2.grabCut(image_rgb, mask, rect, bgd_model, fgd_model,15, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
segmented_image = image_rgb * mask2[:, :, np.newaxis]
plt.figure(figsize=(10, 5))
plt.subplot(121), plt.imshow(image_rgb), plt.title('Ảnh gốc')
plt.axis('off')
plt.subplot(122), plt.imshow(segmented_image), plt.title('Ảnh phân đoạn sử dụng Graph Cuts')
plt.axis('off')
plt.show()

output_path = '/content/drive/MyDrive/Colab Notebooks/segmented_image.jpg' 
plt.imsave(output_path, segmented_image) 
## Prompt 5
you're tourist guide. write me description, activities, famous food, best time to visit base on place i give you. say ok if you are ready
Format:

Tourist Attraction: [Tên địa điểm]
Popular Attractions: [Các địa điểm tham quan nổi bật]
Activities: [Các hoạt động nổi bật]
Famous Food: [Món ăn đặc sản]
Best Time to Visit: [Thời gian tham quan lý tưởng]
## Prompt 6
Tương tự prompt 2 
git add "C:\Users\Thanh An\hoccodeai-baitap\baitap-submit\TranThanhAn\01-prompt-engineering\01-prompt-engineering.md"
git commit -m "Đã hoàn thành bài tập [01-prompt-engineering]"
