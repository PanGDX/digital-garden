# Quartz v4

> “[One] who works with the door open gets all kinds of interruptions, but [they] also occasionally gets clues as to what the world is and what might be important.” — Richard Hamming

Quartz is a set of tools that helps you publish your [digital garden](https://jzhao.xyz/posts/networked-thought) and notes as a website for free.

This is a personal version used for my blog: blog.prantan.work

# Setup method:
**Pre-requisites**
1.  **Node.js** (v18.14 or higher) - Required to build the website.
2.  **Git** - Required to push your notes to a repository.
3.  **A GitHub Account** - Cloudflare Pages will pull your notes from here.
4.  **Cloudflare Account and Working Domain** - To expose the content to the Internet
5.  **Obsidian** - I use Obsidian for my workflow. It converts well to Quartz because both use Markdown (with minor modifications)

**Setup Quartz**
Quartz is the engine that will turn your Markdown files into a functioning website.

1. Open your terminal (Command Prompt/Terminal) and navigate to where you want the code for your website to live (e.g., your Documents folder).
2. Clone the Quartz repository:
   ```bash
   git clone https://github.com/jackyzha0/quartz.git my-digital-garden
   cd my-digital-garden
   ```
3. Install the dependencies:
   ```bash
   npm install
   ```
4. Initialize Quartz:
   ```bash
   npx quartz create
   ```
5. Test it locally:
   ```bash
   npx quartz build --serve
   ```
   Open `http://localhost:8080` in your browser. You should see your notes as a website! Press `Ctrl+C` in the terminal to stop the server when you are done.


**Push to GitHub**
Cloudflare needs a place to pull your website files from. 

1. Go to [GitHub](https://github.com/) and create a new **Private** repository (e.g., `my-digital-garden`). Do *not* initialize it with a README.
2. Go back to your terminal (inside your `my-digital-garden` folder) and link your local folder to GitHub:
   ```bash
   git remote rm origin
   git remote add origin https://github.com/YOUR-GITHUB-USERNAME/my-digital-garden.git
   git add .
   git commit -m "Initial garden setup"
   git push -u origin v4
   ```


**Push to Cloudflare**
1. Log in to your [Cloudflare Dashboard](https://dash.cloudflare.com/).
2. Go to **Workers & Pages** on the left sidebar.
3. Click **Create application**, then select the **Pages** tab.
4. Click **Connect to Git** and authorize Cloudflare to access your GitHub account.
5. Select your `my-digital-garden` repository and click **Begin setup**.
6. **Configure the Build Settings:**
   *   **Project name:** (e.g., `my-digital-garden`)
   *   **Production branch:** `v4` (Quartz uses v4 instead of main)
   *   **Framework preset:** `None`
   *   **Build command:** `npx quartz build`
   *   **Build output directory:** `public`
7. Click **Save and Deploy**. Cloudflare will now build your site. Once finished, it will give you a temporary `*.pages.dev` link.

Since your main website is already on Cloudflare, setting up a subdomain (like `notes.yourdomain.com` or `garden.yourdomain.com`) is seamless.

1. In Cloudflare, go to your newly created Pages project.
2. Click on the **Custom Domains** tab.
3. Click **Set up a custom domain**.
4. Type in the subdomain you want (e.g., `garden.yourdomain.com`).
5. Click **Continue**. Cloudflare will automatically add the necessary CNAME DNS records to your domain since it already manages your DNS.
6. Wait a few minutes for the SSL certificate to generate. Your digital garden is now live on your subdomain!


**Workflow**
- Write ideas down into your own personal Obsidian notes. For select ideas, put them into the /Public folder (or whatever folder you want)
- To update the content, run `syncfiles.py`. Fill in the information as needed. `syncfiles.py` does the following
  - Copies the media needed to the `/content` folder of this repo
  - Replaces any wikilink instance (defaultly used in Obsidian) with proper Markdown syntax
  - Runs the syncing process
