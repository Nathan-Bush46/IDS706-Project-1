# import matplotlib.pyplot as plt
from fpdf import FPDF
from lib import calculate


def print_to_pdf(stats, path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)

    pdf_add_stats(stats, pdf, "stem-height")
    pdf.cell(180, 10, txt="", align="C", border=0, ln=True)
    pdf_add_stats(stats, pdf, "stem-width")

    pdf.image(path + "scatter_plot.png", w=100, type="PNG")
    # save the pdf with name .pdf
    pdf.output(path + "example_stats.pdf")


def pdf_add_stats(stats, pdf, text):
    pdf.cell(180, 10, txt=text, align="C", border=1, ln=True)
    for i in range(len(stats)):
        stat_print = stats[i][0] + " " + str(stats[i][1][text])
        pdf.cell(180, 10, txt=stat_print, align="C", border=1, ln=True)


if __name__ == "__main__":
    print("making image and pdf")
    stats = calculate(
        "./src/main_workspace/data/hw1_q3_test_data.csv",
        "./src/main_workspace/outputs/",
    )
    print_to_pdf(stats, "./src/main_workspace/outputs/")
    print("done: see /outputs")
