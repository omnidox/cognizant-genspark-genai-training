# main.py - Choose GUI at runtime
import sys

if len(sys.argv) > 1 and sys.argv[1] == "pyqt":
    from PyQt6.QtWidgets import QApplication
    from views.pyqt_view import StudyPlannerPyQt
    
    app = QApplication(sys.argv)  # ✅ Create QApplication first!
    window = StudyPlannerPyQt()
    window.show()
    sys.exit(app.exec())  # ✅ Start event loop
else:
    from views.tkinter_view import StudyPlannerTkinter
    
    app = StudyPlannerTkinter()
    app.mainloop()  # ✅ Tkinter uses mainloop()
