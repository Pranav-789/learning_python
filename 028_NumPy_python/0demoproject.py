import streamlit as st
import numpy as np

# Your backend logic (copied directly from your existing code)
class SystemOfLinearEquation:
    def __init__(self, system_matrix):
        self.system = system_matrix
        self.cols = self.system.shape[1] - 1
        self.rows = self.system.shape[0]

    def rowechaelon_conversion(self):
        self.rowechaelon = self.system.copy().astype(float)
        pivot = 0
        i = 0
        while i < len(self.rowechaelon):
            if pivot >= self.rowechaelon.shape[1]:
                break
            if self.rowechaelon[i, pivot] != 0:
                for j in range(i + 1, len(self.rowechaelon)):
                    if self.rowechaelon[j, pivot] == 0:
                        continue
                    else:
                        mult = self.rowechaelon[j, pivot] / self.rowechaelon[i, pivot]
                        self.rowechaelon[j] -= self.rowechaelon[i] * mult
                pivot += 1
                i += 1
            else:
                swapIndex = -1
                for k in range(i + 1, len(self.rowechaelon)):
                    if self.rowechaelon[k, pivot] != 0:
                        swapIndex = k
                        break
                if swapIndex != -1:
                    self.rowechaelon[[i, swapIndex]] = self.rowechaelon[[swapIndex, i]]
                else:
                    pivot += 1
                    i += 1

    def getRankOfMatrix(self):
        rank1 = 0
        rank2 = 0
        for row in self.rowechaelon[:, 0:self.cols]:
            if not np.all(row == 0):
                rank1 += 1

        for row in self.rowechaelon:
            if not np.all(row == 0):
                rank2 += 1

        num_vars = self.system.shape[1] - 1
        result = {
            "system_rank": rank1,
            "augmented_rank": rank2,
            "status": ""
        }

        if rank1 != rank2:
            result["status"] = "❌ The system is inconsistent — no solution."
        elif rank1 == num_vars:
            result["status"] = "✅ Unique solution exists."
        else:
            result["status"] = "♾️ Infinitely many solutions exist."

        return result

# ------------------ Streamlit Frontend ------------------

st.set_page_config(page_title="Linear Equation Solver", layout="centered")
st.title("🧮 Linear Equation Solver using Row Echelon Form")

variable_names = ['x', 'y', 'z', 't', 'p', 'q']

n_vars = st.number_input("Number of variables (max 6)", min_value=1, max_value=6, value=2)
n_eqs = st.number_input("Number of equations", min_value=1, max_value=10, value=2)

st.markdown("---")
st.subheader("Enter coefficients and constants for each equation:")

matrix = []

for i in range(n_eqs):
    st.markdown(f"**Equation {i+1}:**")
    row = []
    cols = st.columns(n_vars + 1)
    for j in range(n_vars):
        row.append(cols[j].number_input(f"{variable_names[j]}", key=f"eq{i}var{j}"))
    row.append(cols[-1].number_input("=", key=f"eq{i}const"))
    matrix.append(row)

matrix_np = np.array(matrix, dtype=float)

if st.button("🔍 Solve"):
    st.subheader("📊 Augmented Matrix:")
    st.write(matrix_np)

    system = SystemOfLinearEquation(matrix_np)
    system.rowechaelon_conversion()

    st.subheader("📐 Row Echelon Form:")
    st.write(np.round(system.rowechaelon, 4))

    st.subheader("📏 Rank Analysis:")
    result = system.getRankOfMatrix()
    st.write(f"System Rank: `{result['system_rank']}`")
    st.write(f"Augmented Matrix Rank: `{result['augmented_rank']}`")

    st.subheader("✅ Result:")
    st.info(result["status"])
