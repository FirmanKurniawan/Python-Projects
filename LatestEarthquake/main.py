"""
Aplikasi Gempa Terkini
MODULARISASI DENGAN FUNCTION
MODULASRISASI DENGAN PACKAGE
"""
import gempaterkini

if __name__ == "__main__":
    result = gempaterkini.ekstraksi_data()
    gempaterkini.tampilkan_data(result)
