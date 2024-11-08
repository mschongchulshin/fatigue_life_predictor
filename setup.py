from setuptools import setup, find_packages

setup(
    name='fatigue_life_predictor',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'fatigue_life_predictor': ['fatigue_life_model.h5']  # .h5 파일 포함
    },
    install_requires=[
        'tensorflow>=2.0',
        'numpy',
        'pandas',
        'scikit-learn'
    ],
    description='LSTM과 Attention을 사용한 피로 수명 예측 라이브러리',
    author='Hongchul Shin',
    author_email='saekomi5@korea.ac.kr',
    url='https://github.com/mschongchulshin/fatigue_life_predictor',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
