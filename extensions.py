extention = input("filename: ").strip().casefold()

if ".gif" in extention:
    print("image/gif")

elif ".jpg" in extention:
    print("image/jpeg")

elif ".jpeg" in extention:
    print("image/jpeg")

elif ".png" in extention:
    print("image/png")

elif ".pdf" in extention:
    print("application/pdf")

elif ".txt" in extention:
    print("text/plain")

elif ".zip" in extention:
    print("application/zip")

else:
    print("application/octet-stream")
