#"files.encoding": "any encoding"


from heapq import nlargest
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from googletrans import Translator
import spacy

#rawdocs = """सैमसंग ने हाल ही में अपने इन-पर्सन MWC 2021 इवेंट को रद्द कर दिया है, इसके बजाय, एक ऑनलाइन-ओनली फॉर्मेट के लिए प्रतिबद्ध है। दक्षिण कोरियाई टेक दिग्गज ने हाल ही में सैमसंग गैलेक्सी MWC वर्चुअल इवेंट के लिए समय और तारीख निर्धारित करते हुए इसे आधिकारिक बना दिया। यह कार्यक्रम 28 जून को 17:15 यूटीसी (22:45 IST) पर आयोजित किया जाएगा और YouTube पर इसका सीधा प्रसारण किया जाएगा। अपनी रिलीज में, सैमसंग का कहना है कि वह अपने "हमेशा विस्तारित गैलेक्सी डिवाइस पारिस्थितिकी तंत्र" पेश करेगा, सैमसंग स्मार्ट डिवाइस सुरक्षा के बढ़ते महत्व के संबंध में नवीनतम तकनीकों और नवाचार प्रयासों को पेश करने की भी योजना बना रहा है। सैमसंग उपयोगकर्ताओं के लिए नए अनुभव और डेवलपर्स के लिए नए अवसर प्रदान करने के लिए स्मार्टवॉच के भविष्य के लिए अपने दृष्टिकोण को भी प्रदर्शित करेगा, सैमसंग ने एक स्मार्टवॉच, एक स्मार्टफोन, एक टैबलेट और एक लैपटॉप के सिल्हूट के साथ घटना के लिए एक छवि भी साझा की।"""


def summarizer(rawdocs):
    translater = Translator()
    stopwords = list(STOP_WORDS)
    #print(stopwords)
    nlp = spacy.load('en_core_web_sm')
    rawdocs = translater.translate(rawdocs, dest="en")
    rawdocs = rawdocs.text
    doc = nlp(rawdocs)
    #print(doc)
    tokens = [token.text for token in doc]
    #print(tokens)
    word_freq = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1

    #print(word_freq)

    max_freq = max(word_freq.values())
    #print(max_freq)

    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq

    #print(word_freq)

    sent_tokens = [sent for sent in doc.sents]
    #print(sent_tokens)

    sent_scores = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]

    #print(sent_scores)

    select_len = int(len(sent_tokens) * 0.3)
    # print(select_len)
    summary = nlargest(select_len, sent_scores, key = sent_scores.get)
    #print(summary)

    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    summary = translater.translate(summary, dest="hi").text
    doc2 = translater.translate(rawdocs, dest="hi").text
    doc2 = nlp(doc2)
    #print(summary)
    #print("Length of original text: ",len(rawdocs.split(' ')))
    #print("Length of summary : ",len(summary.split(' ')))


    return summary, doc2, len(rawdocs.split(' ')), len(summary.split(' '))










