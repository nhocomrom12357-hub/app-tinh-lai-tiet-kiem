import streamlit as st

# Tiêu đề ứng dụng
st.title("💰 Ứng dụng tính lãi tiết kiệm ngân hàng")

st.write("Nhập thông tin tiền gửi để tính số tiền nhận được cuối kỳ.")

# Nhập số tiền
tien_gui = st.number_input(
    "Số tiền gửi (VNĐ)",
    min_value=0,
    value=500000000,
    step=1000000
)

# Nhập lãi suất
lai_suat = st.number_input(
    "Lãi suất (%/năm)",
    min_value=0.0,
    value=6.0,
    step=0.1
)

# Chọn kỳ hạn
ky_han = st.selectbox(
    "Chọn kỳ hạn",
    [1, 3, 6, 9, 12, 24, 36]
)

# Chọn phương pháp
phuong_phap = st.radio(
    "Phương pháp tính",
    ["Lãi đơn", "Lãi kép"]
)

# Đổi lãi suất từ % sang số thập phân
r = lai_suat / 100

# Đổi tháng sang năm
n = ky_han / 12

# Nút tính
if st.button("🧮 Tính tiền lãi"):

    if phuong_phap == "Lãi đơn":

        tien_lai = tien_gui * r * n
        tong_tien = tien_gui + tien_lai

    else:

        tong_tien = tien_gui * (1 + r) ** n
        tien_lai = tong_tien - tien_gui

    st.success("Đã tính toán thành công!")

    st.write("### 📊 Kết quả")

    st.write(
        f"**Tiền gốc:** {tien_gui:,.0f} VNĐ"
    )

    st.write(
        f"**Tiền lãi:** {tien_lai:,.0f} VNĐ"
    )

    st.write(
        f"**Tổng tiền cuối kỳ:** {tong_tien:,.0f} VNĐ"
    )
