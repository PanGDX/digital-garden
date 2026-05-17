---
date: "09-05-2026"
tags:
  - documentation
---

# References

Run
`rsync -av --delete "/home/pran/Documents/Pran's Vault/Public/" ./content/ && npx quartz sync`
To sync

# Notes and Insights

Creating a digital garden from Obsidian and hosting it on Cloudflare is an excellent setup. It’s fast, free (or very cheap), and fully under your control. 

To achieve this natively (supporting Obsidian's `[[wikilinks]]`, tags, and graph view), the best tool available right now is **Quartz (v4)**. It is a highly customizable Static Site Generator built specifically to turn Obsidian vaults into beautiful websites.

Here is the step-by-step guide to setting up your Obsidian Digital Garden next to your Cloudflare-hosted website.

---

### Phase 1: Prerequisites
Before starting, ensure you have the following installed on your computer:
1.  **Node.js** (v18.14 or higher) - Required to build the website.
2.  **Git** - Required to push your notes to a repository.
3.  **A GitHub Account** - Cloudflare Pages will pull your notes from here.

### Phase 2: Prepare Your Obsidian Vault
You probably don't want to publish *everything* in your vault. 
1. Open your Obsidian vault.
2. Create a new folder named `Garden` (or `Public`). Move all the notes you want to publish into this folder. 
3. *Alternative:* You can use a dedicated Obsidian Vault strictly for your digital garden.

### Phase 3: Install and Configure Quartz
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


- Manually create an `index.md` file and put it in content subfolder. Example:

```
---
title: Welcome Home
---
Welcome to my digital garden!
```


1. Test it locally:
   ```bash
   npx quartz build --serve
   ```
   Open `http://localhost:8080` in your browser. You should see your notes as a website! Press `Ctrl+C` in the terminal to stop the server when you are done.

### Phase 4: Push to GitHub
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

### Phase 5: Deploy to Cloudflare Pages
Now, let's get it online.

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

### Phase 6: Make it "Adjacent" to Your Website (Custom Domain)
Since your main website is already on Cloudflare, setting up a subdomain (like `notes.yourdomain.com` or `garden.yourdomain.com`) is seamless.

1. In Cloudflare, go to your newly created Pages project.
2. Click on the **Custom Domains** tab.
3. Click **Set up a custom domain**.
4. Type in the subdomain you want (e.g., `garden.yourdomain.com`).
5. Click **Continue**. Cloudflare will automatically add the necessary CNAME DNS records to your domain since it already manages your DNS.
6. Wait a few minutes for the SSL certificate to generate. Your digital garden is now live on your subdomain!

### Phase 7: Your New Daily Publishing Workflow
You don't need to touch the terminal to update your site anymore. Quartz has a built-in sync tool.

1. Write your notes, create links, and build your knowledge base in your Obsidian `Garden` folder.
2. Open your terminal, navigate to your `my-digital-garden` folder, and type:
   ```bash
   npx quartz sync
   ```
   *This single command automatically commits your changes and pushes them to GitHub.*
3. Cloudflare Pages will detect the change in GitHub, automatically build the new version of your site, and deploy it within a minute.

### 💡 Pro-Tips for your Setup:
*   **Customization:** Open `quartz.config.ts` in your code editor to change the site title, font, colors, and toggle features like the interactive Graph View or Backlinks.
*   **Drafts:** If you are working on a note but don't want it published yet, add `draft: true` to the YAML frontmatter at the top of your Obsidian note. Quartz will ignore it during the build.
*   **Obsidian Git Plugin:** If you want to avoid the terminal entirely, you can install the "Obsidian Git" plugin inside Obsidian and configure it to automatically push your changes to GitHub on a schedule.




A symlink is essentially just a "shortcut" that points to a folder on your physical hard drive. When you pushed your Quartz folder to GitHub, Git didn't upload your actual Obsidian notes—it only uploaded the shortcut. 

When Cloudflare builds your website, it tries to follow that shortcut. But because Cloudflare's servers don't have access to your local computer's hard drive, it finds nothing, builds an empty website, and gives you a **404 error**. 

Additionally, the `Warning: couldn't find git repository for content` error happens because Quartz looks at your Git history to automatically determine the "Last Modified" and "Created" dates for your notes. Because the symlink points outside the Git repository, it can't find that history.

Here is exactly how to fix it.

### Step 1: Remove the Symlink
First, we need to get rid of the shortcut.
1. Open your terminal and navigate to your `my-digital-garden` folder.
2. Delete the symlinked folder by running:
   * **Mac/Linux:** `rm -rf content`
   * **Windows:** `rmdir /s /q content`
3. Create a normal, real folder in its place:
   ```bash
   mkdir content
   ```

### Step 2: Choose Your Workflow

#### Option B: The "Copy & Sync" Method (If you want to keep your current Vault)
If you want to keep your garden notes inside your existing, larger Obsidian vault, you cannot use a symlink. Instead, you must **copy** the files over right before you publish. 

You can make this painless by creating a command that copies the files and syncs them to GitHub all at once.
1. Delete the contents of the Quartz `content` folder.
2. Copy your notes from your Obsidian `Garden` folder and paste them into the Quartz `content` folder.
3. Every time you want to publish an update, you will need to copy the files over. You can automate this in your terminal:
   * **Mac/Linux:** 
     `rsync -av --delete /path/to/Obsidian/Garden/ ./content/ && npx quartz sync`

For me that would be
`rsync -av --delete "/home/pran/Documents/Pran's Vault/Public/" ./content/ && npx quartz sync`
Note `/Public/` which copies the files rather than the folder.

   * **Windows (Command Prompt):** 
     `robocopy "C:\path\to\Obsidian\Garden" "C:\path\to\my-digital-garden\content" /MIR & npx quartz sync`

### Step 3: Push the Real Files to Cloudflare
Once you have physical `.md` files inside the `my-digital-garden/content` folder (using either Option A or Option B), run your sync command again:

```bash
npx quartz sync
```

**What will happen now:**
1. Git will finally see the actual Markdown files and upload them to GitHub.
2. The `couldn't find git repository` warning will disappear because the files are now physically inside the repository.
3. Cloudflare will detect the new files on GitHub, rebuild your site, and your content will appear instead of the 404 page!
