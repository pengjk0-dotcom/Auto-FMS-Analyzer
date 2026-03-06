from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import shutil
import os

# 引入你的算法模块
from fms_scorer import DeepSquatAnalyzer
# from pose_detector import PoseDetector # 如果还没写好这个类，可以先注释掉

app = FastAPI()

# 允许前端跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "FMS AI Backend is running!"}

@app.post("/analyze")
async def analyze(video: UploadFile = File(...)):
    # 1. 保存上传的视频
    temp_file = f"temp_{video.filename}"
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)
        
    # 2. TODO: 这里调用你的 PoseDetector 和 Analyzer
    # scores, advice = your_pipeline.process(temp_file)
    
    # 3. 模拟返回数据 (为了让前端先跑通)
    import random
    fake_score = random.choice([1, 2, 3])
    
    # 4. 清理临时文件
    if os.path.exists(temp_file):
        os.remove(temp_file)
        
    return {
        "status": "success",
        "score": fake_score,
        "details": ["检测到躯干前倾", "膝盖内扣风险"],
        "improvements": ["建议加强核心力量", "通过臀桥训练激活臀大肌"]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)