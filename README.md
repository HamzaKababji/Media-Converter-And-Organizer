
<br/>
<div align="center">
  <h1 id = readme-top>Media Converter And Organizer</h1>
</div>


<details>
  <summary><b>Table of Contents</b></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#installation">Installation</a>
    </li>
    <li><a href="#key-features">Key Features</a></li>
    <li><a href="#future-expansions">Future Expansions</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>
<br/>


## About The Project

As someone with a lot of photos and videos, most of which being taken on an iPhone, there was a necessity for a converter to be able to view .MOV and .HEIC media on my laptop and/or storage device such as TNAS; while also having to organize those same tens of thousands of photos and videos scattered around dating back all the way to 2004.

Thus, this idea came to my father and I's mind and I went ahead with the execution of it. After some struggles throughout the development process, and running into a lot of issues with the packaging of the software into a .exe file, I was able to pull through and succeed! Furthermore, I decided to document my project on GitHub because I am sure many others are in the same shoes where they are IN NEED of such a software as they do not want to spend 100s on a storage device just to worry about more issues that might come their way, such as monthly subscriptions, limitations on space, etc...

Therefore, as long as you have a laptop or a PC that you are able to use, you can follow the installation steps below to set up this application and take matters into your own hands in cleaning up your media!


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Installation

_Until I publish this software on the Microsoft Store (Hopefully), you will have to follow the below installation steps to use this application. I assume you already know how to run some python code and have pip installed._

#### 1. Open Terminal and Clone the Repo
   ```bash
   git clone https://github.com/HamzaKababji/Media-Converter-And-Organizer.git
   ```
   <br />

#### 2. Open Project in VS Code

<p align="center">
  <img src="ReadMeAssets\image1.png" alt="First Image" width="45%"align="center"/>
  <img src="ReadMeAssets\image2.png" alt="Second Image" width="45%"align="center"/>
</p>

<br />

#### 3. Open Terminal Window in Project Location

<p align="center">
  <img src="ReadMeAssets\image3.png" alt="Third Image" width="100%"align="center"/>
</p>

<br />

#### 4. Install any Required Dependencies in Your Environment

   ```bash
    pip install Pillow
   ```

   ```bash
      pip install pillow_heif
   ```

   ```bash
    pip install hachoir
   ```

   **You MUST also install ffmpeg.exe by going to [this](https://ffmpeg.org/download.html) link and then replace the file path in Organizer.py Line 20.**

   <br/>

   _You may need to install more packages depending on your system. If so, follow terminal instructions and search online for the steps to do so._

<br />

#### 5. Run the Gui.py file


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Key Features
<p align="center">
  <img src="ReadMeAssets\image4.png" alt="Fourth Image" width="100%"align="center"/>
</p>

 - Easy to use interface, with a progress bar and terminal pop-up window.
 - Converts .MOV or .mov to .mp4
 - Converts .HEIC or .heic to .jpeg
 - Parses through every single file in a folder (Even in SUBFOLDERS!).
 - Organizes all media based on the date taken property.
 - If the date taken does not exist, takes the date modified property.
 - Works well with network storages!
 - Very robust and thoroughly tested system (Tested for 10s of thousands of files).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Future Expansions

 - Explore opportunities to publish on the Microsoft Store.
 - Implement Multi-Processing to further optimize performance.
 - Possibly implement AI detection for duplicated photos.
 - Expand to other operating systems.
 - Regularly fix any bugs that might occur.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## License

Distributed under the MIT License. See [License](https://github.com/HamzaKababji/Media-Converter-And-Organizer/blob/main/LICENSE) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Contact

Hamza Elkababji - [Personal Website](https://hamzakababji.neuralcity.ca/) - [LinkedIn](https://www.linkedin.com/in/hamzakababji/) - [GitHub](https://github.com/HamzaKababji) - [X](https://twitter.com/hamza_kababji) - hamza.kababji@gmail.com

Project Link: [Media Converter And Organizer](https://github.com/HamzaKababji/Media-Converter-And-Organizer)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
