git lfs install
git lfs track "*.h5"
git add .gitattributes
git commit -m "Track .h5 files with Git LFS"
git add pneumonia_detection_model.h5
git commit -m "Add large .h5 file using Git LFS"
git push origin main  # or your branch name
