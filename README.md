## Problem Statement

Industri perawatan kecantikan telah berkembang pesat dan produk perawatan kulit menjadi salah satu produk yang paling dicari oleh konsumen. Di era digital saat ini, konsumen seringkali mencari ulasan produk sebelum memutuskan untuk membeli. Namun, tidak semua ulasan dapat dipercaya dan kadang-kadang sulit untuk membedakan ulasan yang benar-benar terverifikasi dengan ulasan yang tidak terverifikasi. Oleh karena itu, perlu adanya sebuah sistem yang dapat membantu konsumen untuk membedakan ulasan yang terverifikasi dengan ulasan yang tidak terverifikasi.

## Objective

Tujuan dari proyek ini adalah untuk membangun sebuah model Natural Language Processing (NLP) yang dapat memprediksi ulasan produk perawatan kulit dari Ulta Beauty dan membedakan ulasan yang terverifikasi dengan ulasan yang tidak terverifikasi. Model ini akan menggunakan dataset ulasan produk yang diambil dari situs web Ulta Beauty. Dengan menggunakan model NLP, diharapkan dapat memprediksi sentimen positif, negatif, atau netral dari ulasan produk perawatan kulit yang diberikan oleh konsumen dan menandai apakah ulasan tersebut terverifikasi atau tidak terverifikasi. Hal ini akan membantu konsumen dalam memilih produk perawatan kulit dan meningkatkan kepercayaan konsumen terhadap ulasan produk yang diberikan.

## Conclusion
*  Tujuan bisnisnya adalah untuk memaksimalkan jumlah review yang diklasifikasikan dengan benar sebagai verified, maka metrik evaluasi yang tepat adalah recall. Recall mengukur seberapa baik model dalam menemukan semua instance dari kelas positif (dalam hal ini, review yang sebenarnya telah diverifikasi) dari semua instance yang sebenarnya positif. Sehingga, recall akan memberikan informasi tentang seberapa baik model dapat mengidentifikasi review yang sebenarnya telah diverifikasi dari semua review yang sebenarnya telah diverifikasi.
* Setelah dilakukan beberapa cara dalam pengerjaan model, model masih tidak dapat bekerja dalam memprediksi dengan baik.
* Jika di lihat dari dataset dan melihat dari analysis EDA yang telah dilakukan sebagai verifide buyer masih bisa memberikan review negative, verified buyer tidak selalu memberikan review yang positif,makadari itu tidak ada pembanding cukup signifikan dalam melakukan data uji oleh mechine.sehingga menurut saya ini bisa menjadi salah satu indikasi bahwa model tidak dapat memprediksi dengan baik.
* Dataset berikut terdapat label atau data yang tidak seimbang, dalam preprocess telah menggunakan teknik seperti undersampling untuk mengatasi masalah ini, tetapi model masih tidak cukup baik
* metode yang digunakan dalam preprocessing dapat menghasilkan representasi yang memadai dan relevan dari dokumen atau teks yang akan diproses. Metode yang digunakan dalam preprocessing dapat mencakup tokenisasi, penghilangan stop word, stemming, dan pembuatan n-gram.

*hasil prediksi yang masih masih tidak baik meskipun sudah melakukan beberapa model berikut adalah cara yang bisa di coba:*

* jika di lihat dari data base ini data cenderung sedikit sehingga bisa menambahkan data training. Semakin banyak data yang digunakan untuk melatih model, semakin akurat model yang dihasilkan.
* tambahkan fitur-fitur baru. Fitur-fitur baru yang relevan dapat membantu meningkatkan performa model.
* melakukan Lakukan augmentasi data. Jika dataset yang digunakan terlalu kecil atau tidak cukup representatif, maka augmentasi data dapat dilakukan dengan membuat variasi dari dataset yang ada atau dengan membuat dataset baru yang sejenis.

## Columns

* Review Title: The title of the review.
* Review_Text: The full text of the review.
* Verified_Buyer: Whether the reviewer is a verified buyer of the product.
* Review_Date: The date the review was published relative to the review scrape date.
* Review_Location: The location of the reviewer.
* Review_Upvotes: How many times the review was upvoted by other reviewers.
* Review_Downvotes: How many times the review was downvoted by other reviewers.
* Product: The name of the product the review was issued for.
* Brand: The brand of the product.
* Scrape Date: The date the data was pulled from the web.
* Sources: https://www.kaggle.com/datasets/nenamalikah/nlp-ulta-skincare-reviews
