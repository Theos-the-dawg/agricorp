# # Create Memorandum (Marking Guide) for KM-01-KT01 Pop Quiz (45 Marks)

# from docx import Document
# from docx.enum.text import WD_ALIGN_PARAGRAPH
# from docx import *

# document = Document()

# # Title
# title = document.add_heading('KM-01-KT01: Systems Analysis and Design', level=1)
# title.alignment = WD_ALIGN_PARAGRAPH.CENTER

# document.add_heading('MEMORANDUM / MARKING GUIDE (45 MARKS)', level=2)

# # SECTION A
# document.add_heading('SECTION A: MULTIPLE CHOICE (10 MARKS)', level=3)

# mcq_answers = [
#     "1. C (Profit) – (2)",
#     "2. B (Define WHAT the system must do) – (2)",
#     "3. C (Economic feasibility) – (2)",
#     "4. C (A storage location) – (2)",
#     "5. B (Horizontal scaling) – (2)"
# ]

# for ans in mcq_answers:
#     document.add_paragraph(ans)

# # SECTION B
# document.add_heading('SECTION B: SHORT ANSWER QUESTIONS (15 MARKS)', level=3)

# document.add_paragraph("6. Define a system. (3)")
# document.add_paragraph("A system is an organized collection of interrelated and interdependent components that work together to achieve a common objective. (3)")

# document.add_paragraph("\n7. List and briefly explain any THREE properties of a system. (6)")
# document.add_paragraph("Award 2 marks each (1 mark for identification + 1 mark for explanation).")
# document.add_paragraph("Possible answers:")
# document.add_paragraph("• Organization – Structured arrangement of components.")
# document.add_paragraph("• Interaction – Components communicate/work together.")
# document.add_paragraph("• Interdependence – Subsystems rely on one another.")
# document.add_paragraph("• Integration – System functions as a unified whole.")
# document.add_paragraph("• Central Objective – System has a clear overall goal.")

# document.add_paragraph("\n8. Differentiate between Functional and Non-Functional Requirements. (4)")
# document.add_paragraph("Functional Requirements – Specific behaviors/functions the system must perform. (2)")
# document.add_paragraph("Non-Functional Requirements – Performance, security, scalability, and quality attributes of the system. (2)")

# document.add_paragraph("\n9. State TWO fact-finding techniques used in system analysis. (2)")
# document.add_paragraph("Any TWO of the following (1 mark each):")
# document.add_paragraph("• Interviews")
# document.add_paragraph("• Observation")
# document.add_paragraph("• Questionnaires")
# document.add_paragraph("• Document review")
# document.add_paragraph("• Workshops")
# document.add_paragraph("• Prototyping")

# # SECTION C
# document.add_heading('SECTION C: STRUCTURED QUESTIONS (20 MARKS)', level=3)

# document.add_paragraph("10. SDLC Phases (6)")
# document.add_paragraph("Award 1 mark each for correct phase + brief explanation.")
# document.add_paragraph("• Planning – Identify need and feasibility.")
# document.add_paragraph("• Analysis – Define requirements (WHAT system must do).")
# document.add_paragraph("• Design – Plan technical solution (HOW system will work).")
# document.add_paragraph("• Development – Build/program the system.")
# document.add_paragraph("• Implementation – Deploy/install system.")
# document.add_paragraph("• Maintenance – Ongoing support and improvements.")

# document.add_paragraph("\n11.1 Explain the importance of conducting a feasibility study. (4)")
# document.add_paragraph("• Determines project viability. (1)")
# document.add_paragraph("• Identifies risks and constraints. (1)")
# document.add_paragraph("• Ensures wise investment of resources. (1)")
# document.add_paragraph("• Prevents project failure. (1)")

# document.add_paragraph("\n11.2 List five (5) types of feasibility studies and describe them. (10)")
# document.add_paragraph("Award 2 marks each (1 mark for type + 1 mark for explanation).")
# document.add_paragraph("• Operational Feasibility – Assesses user acceptance and organizational fit.")
# document.add_paragraph("• Technical Feasibility – Evaluates availability of required technology and expertise.")
# document.add_paragraph("• Economic Feasibility – Cost-benefit analysis of the project.")
# document.add_paragraph("• Schedule Feasibility – Determines if project can be completed on time.")
# document.add_paragraph("• Cultural Feasibility – Checks alignment with organizational culture.")
# document.add_paragraph("• Legal Feasibility – Ensures compliance with laws and regulations.")
# document.add_paragraph("Any FIVE accepted.")

# document.add_paragraph("\nTOTAL: 45 MARKS")

# # Save file
# #file_path = "/mnt/data/KM-01-KT01_Pop_Quiz_Memorandum_45_Marks.docx"
# file_path = "C:/Users/mothe/Desktop/KM-01-KT01_Pop_Quiz_Memorandum_45_Marks.docx"
# document.save(file_path)

# file_path
