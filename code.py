import tkinter as tk


def add_patient():
    name = patient_name_entry.get()
    disease = disease_entry.get()
    room_fee_rupees = float(room_fee_entry.get())
    medicinal_bill_rupees = float(medicinal_bill_entry.get())
    doctor_fee_rupees = float(doctor_fee_entry.get())
    entry_date = entry_date_entry.get()
    leave_date = leave_date_entry.get()

    patient_data = {
        "Name": name,
        "Disease": disease,
        "Room Fee (Rupees)": room_fee_rupees,
        "Medicinal Bill (Rupees)": medicinal_bill_rupees,
        "Doctor Fee (Rupees)": doctor_fee_rupees,
        "Entry Date": entry_date,
        "Leave Date": leave_date
    }

    patients.append(patient_data)
    patient_listbox.insert(tk.END, name)

    clear_entries()


def show_patient_info():
    selected_index = patient_listbox.curselection()
    if not selected_index:
        return

    selected_patient = patients[selected_index[0]]
    room_fee_rupees = selected_patient['Room Fee (Rupees)']
    medicinal_bill_rupees = selected_patient['Medicinal Bill (Rupees)']
    doctor_fee_rupees = selected_patient['Doctor Fee (Rupees)']
    entry_date = selected_patient['Entry Date']
    leave_date = selected_patient['Leave Date']

    total_bill_rupees = room_fee_rupees + medicinal_bill_rupees + doctor_fee_rupees

    info_window = tk.Toplevel(root)
    info_window.title(f"Patient Information: {selected_patient['Name']}")
    info_label = tk.Label(info_window, text=f"Patient Name: {selected_patient['Name']}\n"
                                            f"Disease: {selected_patient['Disease']}\n"
                                            f"Room Fee (Rupees): ₹{room_fee_rupees:.2f}\n"
                                            f"Medicinal Bill (Rupees): ₹{medicinal_bill_rupees:.2f}\n"
                                            f"Doctor Fee (Rupees): ₹{doctor_fee_rupees:.2f}\n"
                                            f"Entry Date: {entry_date}\n"
                                            f"Leave Date: {leave_date}\n"
                                            f"Total Bill (Rupees): ₹{total_bill_rupees:.2f}")
    info_label.pack()

def clear_entries():
    patient_name_entry.delete(0, tk.END)
    disease_entry.delete(0, tk.END)
    room_fee_entry.delete(0, tk.END)
    medicinal_bill_entry.delete(0, tk.END)
    doctor_fee_entry.delete(0, tk.END)
    entry_date_entry.delete(0, tk.END)
    leave_date_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Hospital Management System")


patient_name_label = tk.Label(root, text="Patient Name:")
patient_name_label.pack()
patient_name_entry = tk.Entry(root)
patient_name_entry.pack()

disease_label = tk.Label(root, text="Disease:")
disease_label.pack()
disease_entry = tk.Entry(root)
disease_entry.pack()


room_fee_label = tk.Label(root, text="Room Fee (Rupees):")
room_fee_label.pack()
room_fee_entry = tk.Entry(root)
room_fee_entry.pack()

medicinal_bill_label = tk.Label(root, text="Medicinal Bill (Rupees):")
medicinal_bill_label.pack()
medicinal_bill_entry = tk.Entry(root)
medicinal_bill_entry.pack()

doctor_fee_label = tk.Label(root, text="Doctor Fee (Rupees):")
doctor_fee_label.pack()
doctor_fee_entry = tk.Entry(root)
doctor_fee_entry.pack()


entry_date_label = tk.Label(root, text="Entry Date:")
entry_date_label.pack()
entry_date_entry = tk.Entry(root)
entry_date_entry.pack()

leave_date_label = tk.Label(root, text="Leave Date:")
leave_date_label.pack()
leave_date_entry = tk.Entry(root)
leave_date_entry.pack()

add_button = tk.Button(root, text="Add Patient", command=add_patient)
add_button.pack()


patient_listbox = tk.Listbox(root)
patient_listbox.pack()

show_info_button = tk.Button(root, text="Show Patient Info", command=show_patient_info)
show_info_button.pack()


patients = []

root.mainloop()