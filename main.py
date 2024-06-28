import tkinter as tk
from tkinter import scrolledtext
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

def generate_wordclouds():
    resume_text = resume_textbox.get("1.0", tk.END)
    job_listing_text = job_listing_textbox.get("1.0", tk.END)

    resume_wc = WordCloud(width=300, height=300, background_color='white').generate(resume_text)
    job_listing_wc = WordCloud(width=300, height=300, background_color='white').generate(job_listing_text)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(resume_wc, interpolation='bilinear')
    plt.axis('off')
    plt.title("Resume Word Cloud")

    plt.subplot(1, 2, 2)
    plt.imshow(job_listing_wc, interpolation='bilinear')
    plt.axis('off')
    plt.title("Job Listing Word Cloud")

    plt.show()



