# How to Check if Your macOS is 32-bit or 64-bit

Although Apple has fully transitioned to 64-bit macOS for many years, some users—especially those running older Intel-based Macs—may still need to confirm whether their system or specific apps are 32-bit or 64-bit. 

![](D:\f\Documents\Github\Junbo-PARA-Notes\Project\how-to-check-your-macos-32-bit-or-64-bit.png)

This post will guide you though how to check if your macOS is 32 bit or 64-bit.

------

## Content

1. macOS Is a 64-bit Operating System by Default
2. Identify CPU Architecture: Intel vs Apple Silicon
3. Use Terminal to Check System Architecture
4. How to Check Whether Apps Are 64-bit or 32-bit
5. Common Pitfalls
6. TL;DR

------

### 1. macOS Is a 64-bit Operating System by Default (Since macOS Catalina)

Starting from **macOS Catalina (10.15)**, Apple **dropped support for all 32-bit apps**, and the operating system itself is exclusively 64-bit. If you're running Catalina or later, your **OS and apps must be 64-bit**.

You can verify your macOS version by clicking:

> **Apple Menu → About This Mac**

Check the **version number** (e.g., 10.15 = Catalina, 11 = Big Sur, 12 = Monterey, etc.).

![check-macos-version-from-settings](D:\f\Documents\Github\Junbo-PARA-Notes\Project\check-macos-version-from-settings.png)

------

### 2. Identify CPU Architecture: Intel vs Apple Silicon

The CPU architecture tells you whether your Mac is using Intel (x86_64) or Apple Silicon (arm64). Both support 64-bit, but some low-level behaviors differ.

#### ➤ Step-by-step:

1. Click the **Apple Menu → About This Mac**

2. Look under **"Chip"** or **"Processor"**:

   - If it says **Apple M1/M2/M3**, then you're using **ARM64 architecture**, 64-bit only.
   - If it says **Intel Core i5/i7/etc.**, you're on **x86_64**, and should check further.

   Here is the cheat table:
   
   ![](D:\f\Pictures\how-to-check-macos-32-or-64-bit\check-mac-cpu-type-from-settings.png)

------

### 3. Use Terminal to Check System Architecture

If you're comfortable with the Terminal, use this command:

```bash
uname -m
```

**Interpretation:**

- `x86_64` → 64-bit Intel CPU
- `arm64` → 64-bit Apple Silicon (M1, M2, etc.)
- `i386` → 32-bit Intel CPU (rare, ancient Macs only)

You can also check the CPU architecture explicitly using:

```bash
sysctl -n machdep.cpu.brand_string
```

This will return something like:

```
Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
```

------

### 4. How to Check Whether Apps Are 64-bit or 32-bit (Only on pre-Catalina)

If you're on **macOS Mojave (10.14)** or earlier, you might still be able to run 32-bit apps.

#### Here's how to check which apps are 32-bit:

1. Click  **About This Mac → System Report**

2. Under **Software**, click **Applications**

3. Wait for it to load (can take a few seconds)

4. Look at the column **“64-Bit (Intel)”**

   - If it says **Yes**, the app is 64-bit
   - If it says **No**, the app is 32-bit and **won’t work on Catalina or newer**

   ![](D:\f\Pictures\how-to-check-macos-32-or-64-bit\check-macos-app-32-bit-or-64-bit.png)

------

### 5. Common Pitfalls

- macOS itself hasn’t been 32-bit for **over a decade**—only very old versions like Snow Leopard or Leopard were.
- Confusing the **CPU architecture** with **app architecture** is common. Even a 64-bit Mac may have 32-bit apps (before Catalina).
- Some command-line tools may still run as 32-bit binaries if manually compiled that way.

------

### 6. TL;DR

| Checkpoint            | What to Look For                     |
| --------------------- | ------------------------------------ |
| macOS Version         | 10.15+ = 64-bit only                 |
| CPU Type (`uname -m`) | `x86_64` or `arm64` = 64-bit         |
| App Compatibility     | Check “System Report → Applications” |

