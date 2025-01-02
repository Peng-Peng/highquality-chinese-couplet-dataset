# highquality-chinese-couplet-dataset

## Summary

这个数据集包含了2250条对句，来自三本经典的古代声韵格律启蒙读物，分别是《声律启蒙》、《笠翁对韵》、《训蒙骈句》。

This dataset contains 2,250 high quality couplets drawn from three classic ancient Chinese phonetics and poetic meter: Sheng Lü Qi Meng (Introduction to Rhymes and Metrics), Li Weng Dui Yun (Li Weng's Rhyming Couplets), and Xun Meng Pian Ju (Paired Sentences for Enlightening Beginners). These three books are considered foundational textbooks for teaching children the art of parallelism in classical Chinese literature.

## How to Use the Dataset
**NOTE: This dataset is provided under the MIT License. Attribution is required in any publications or derivative works.**

这个数据集每个文件夹包含
- 原文：保持了原书的分篇，以方便订正和勘误.
- dataset：每一json file对应原书的一篇, 方便数据集的后续处理。比如可将所有的"一东"韵集合并到一起。
- 每本书的process script: 用于将原文转换为dataset的脚本。Example usage: `python 声律启蒙/process.py`

This dataset is organized into folders containing the following:
- Original Texts: The texts are preserved in their original chapter divisions to facilitate corrections and verification against the source material.
- Dataset: Each JSON file corresponds to a single chapter from the original book, making subsequent processing more convenient. For example, you can merge all json files belong to the "Yi Dong" rhyme into a single dataset.
- Processing Scripts for Each Book: Scripts that convert the original text into the dataset are included. Example usage: `python 声律启蒙/process.py`.


## More Context
-《声律启蒙》作者车万育，清朝康熙年间人。这本书是从前训练儿童应对，掌握声韵格律的启蒙读物。按韵分编，包罗天文、地理、花木、鸟兽、人物、器物等的虚实应对。从单字对到双字对，三字对、五字对、七字对到十一字对，声韵协调，琅琅上口，从中得到语音、词汇、修辞的训练。从单字到多字的层层属对，读起来，如唱歌般。较之其它全用三言、四言句式更见韵味。这类读物，在启蒙读物中独具一格，经久不衰。
明清以来，如《训蒙骈句》、《笠翁对韵》等书，都是采用这种方式编写，并得以广泛流传。

Sheng Lü Qi Meng: Written by Che Wanyu during the Qing Dynasty. This book was a primer for training children in matching words and mastering phonetic tones and metrics. Organized by rhymes, it encompasses topics such as astronomy, geography, flora, fauna, people, and objects. The couplets progress from single-word matches to double, triple, five-word, seven-word, and even eleven-word matches, achieving tonal harmony and an elegant cadence. Reading the lines feels akin to singing, offering training in phonetics, vocabulary, and rhetoric. Compared to other primers that exclusively use three-character or four-character patterns, this work stands out with its distinctive rhythm and enduring appeal. Since the Ming and Qing dynasties, similar works such as Xun Meng Pian Ju and Li Weng Dui Yun have adopted this style, enjoying widespread popularity.

-《笠翁对韵》作者李渔，是他仿照《声律启蒙》写的旨在作诗的韵书，是用于儿童音韵启蒙的书

Authored by Li Yu, this book was modeled after Sheng Lü Qi Meng and designed as a rhyming guide for poetry composition. It served as a phonetic primer for children.

-《训蒙骈句》,明代司守谦撰。骈句，即骈偶句，即对仗句。两马并驾为骈，二人并处为偶，意谓两两相对。古时宫中卫队行列月仗（仪仗），仪仗两两相对，故卞偶亦称对仗。以偶句为主构成字数相等的上下联，上下联词语相对，平仄相对。用这种形式的四六句写成的文章，晚唐时称作“四六”，宋明沿用，至清改称骈体。对童蒙进行骈句训练，为作文作诗建立根基。《训蒙骈句》按韵部顺次，由三言、四言、五言、七言、十一言的五对骈句组成一段，每韵三段。此书与《声律启蒙》、《笠翁对韵》当可为吟诗作对之基，爱好诗文者，若熟而能诵，必大利于笔。历来也是作为训练儿童的语文教材。

Written by Si Shouqian during the Ming Dynasty, this book focuses on paired sentences (also known as parallel sentences or couplets). The term "pian" refers to two horses yoked side by side or two individuals standing together, symbolizing symmetry and parallelism. In ancient times, ceremonial guards in imperial processions formed paired ranks, hence the use of pian to describe matched sentences. Each section features five paired sentences, ranging from three-character to eleven-character lines, organized by rhyme group, with three sections per rhyme. This format aimed to train children in crafting parallel sentences, establishing a foundation for essay and poetry writing. Together with Sheng Lü Qi Meng and Li Weng Dui Yun, this book is an essential resource for poetry enthusiasts. Mastering its content provides significant benefits for literary composition and has traditionally been used as a language textbook for children.



## Future Work:
- 除了以上三部最经典的书籍，还可以加入其他的声韵格律启蒙读物，比如《学对歌诀》、《声律发蒙》等等。In addition to the three most classic works mentioned above, please feel free to expand to other books, such as Xue Dui Ge Jue (The Song of Learning Couplets) and Sheng Lü Fa Meng (Introduction to Prosody), among others.
- 参考资料 References：
1. http://www.360doc.com/content/12/0219/14/1631197_187815759.shtml
2. https://hudsonchinese.wordpress.com/wp-content/uploads/2015/02/e5a3b0e99fb5e99b86e68890.pdf
