
# Pygame UI README

[![Licence](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

[Pygame UI](https://github.com/RednaxGaming/pygame_ui) is a package for building user interfaces for [pygame](https://www.pygame.org/) in JSON.

It is currently a work in progress, but if you wanna test it out, feel free to do so :)

## Table Of Content

- [Quick Start](#quick-start)
   - [Installation](#installation)
   - [Setup](#setup)
      - [Python](#python-file)
      - [JSON](#json-file)
- [Element List](#element-list)
- [Attribute List](#attribute-list)
   - [General](#general)
   - [Frame](#frame)
   - [Label](#label)
   - [Text Input](#text-input)
   - [Button](#button)
   - [Switch](#switch)
   - [Slider](#slider)
- [Frames](#frames)
   - [Frame Path](#frame-path)
- [Examples](#examples)
- [FAQ](#faq)

## Quick Start

### Installation

Pygame UI is available on PyPi:

```shell
pip install pygame-json-ui
```
In case this doesn't work, you'll need to manually add the pygame_ui folder to your site-packages.

When this is done you can test your installation, by executing the following:
```python
>>> import pygame_ui
>>> pygame_ui.test()
Successfully installed! enjoy :)
Version: x.x.x.x
```

### Setup

You will have two files in the same folder:
- whatever.py
- Interface.json <-- Name for automatically loading the file

If you prefer a different name for the json file, or Pygame UI is having issues locating it automatically, you can pass the absolute path to it's parent folder as an argument for `pygame_ui.init()`.

Here a simple example for making a label:

#### Python File

Notice that the `event_handler` is not required unless you want interactive elements to function as expected.

```python
import pygame
import pygame_ui

# Creating a window
pygame.init()
screen = pygame.display.set_mode((1280, 720), vsync=1)
pygame.display.set_caption("GUI")
clock = pygame.time.Clock()


# Initializing interface
Interface = pygame_ui.init()


while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         quit()
      # Call event handler
      Interface.event_handler(event)

   screen.fill((0,0,0))

   # Draw interface
   Interface.draw(screen)

   pygame.display.flip()
   clock.tick(60)
```

#### JSON File
MUST be named `Interface.json` and in the same folder as python file for loading the json file automatically!

```json
{
   "test_label": {
      "type": "label",
      "position": [200,100],
      "size": [120,80],
      "background_color": [200,0,0],
      "text": "IT WORKS!",
      "font_size": 20,
      "auto_size": true
   }
}
```

## Element List

All of the following items will be refered to as `elements`:
- Frame
- Label
- Text Input
- Button
- Switch
- Slider
- Dropdown (Coming soon)

## Attribute List
- `attribute: data type` description (default value).
### General
These attributes can be given to any element type
- `type: str` REQUIRED, specifies which element this is choose from [this](#element-list) list.
- `position: [x,y]` Sets position from top-left of screen to top-left of element boundry box ([0, 0]).
- `position_anchor: str` "top/center/bottom left/center/right" or "center" ("top left").
- `position_relative: bool` Whether given position will be interpreted as relative to parent or absolute (false).
- `size: [x,y]` Sets the size of the element boundry box ([0, 0]).
- `background_color: (r,g,b)` The boundry box will be filled with this color (none).
- `is_visible: bool` (true).
- `is_hoverable: bool` (false).
- `is_clickable: bool` (false).

### Frame
- `contents: {}` See [frames](#frames) for more info.

### Label

- `text: str` Exactly what you think it is.
- `text_color: (r,g,b)` ([255,255,255])
- `text_aa: bool` anti-aliasing (true)
- `font_name: str` ('Arial')
- `font_size: int` (10)
- `font_bold: bool` (false)
- `font_italic: bool` (false)
- `auto_size: bool` This will overwrite size of the boundry box to fit the text within (false).

### Text Input

- `typing_start_on_click: bool` Will set typing to True when the hitbox is clicked (true).
- `typing_end_on_enter: bool` Will set typing to False when `enter` is pressed (true).
- `typing: bool` Whether or not the users button presses will be processed (false).
- `text: str` The currently typed string ("Your text here").
- `caret: bool` Only used for backend (false).
- `caret_timer: float` Only used for backend (0).

### Button

- `contents: {}` The button is basically just a frame with the following default attributes added to it. Making a button manually from a frame is possible, but deprecated.
- `is_clickable: bool` (true)
- `is_hoverable: bool` (true)
- `click_start: bool` (false)
- `click_end: bool` (false)
- `click_held: bool` (false)
- `hover_start: bool` (false)
- `hover_end: bool` (false)
- `hover_held: bool` (false)

### Switch
- `state: bool` Represents the current state of the switch on/off (false)
- `preset: str` A preset for it's looks. Only existing preset is currently: "simple" (none)
- `is_clickable: bool` (true)
- `is_hoverable: bool` (true)
- `click_start: bool` (false)
- `click_end: bool` (false)
- `click_held: bool` (false)
- `hover_start: bool` (false)
- `hover_end: bool` (false)
- `hover_held: bool` (false)

### Slider
- `value_min: int/float` Lower end of the slider (0)
- `value_max: int/float` Uppper end of the slider (1)
- `value: int/float` Represents the current value of the slider (0)
- `preset: str` A preset for it's looks. Only existing preset is currently: "simple" (none)
- `is_clickable: bool` (true)
- `is_hoverable: bool` (true)
- `click_start: bool` (false)
- `click_end: bool` (false)
- `click_held: bool` (false)
- `hover_start: bool` (false)
- `hover_end: bool` (false)
- `hover_held: bool` (false)

## Frames

Frames can contain `elements` Just like how a folder can contain files and other folders.
Frames can also hold other frames, and yes, those can contain frames aswell (see [Frame-ception](#frame-ception)). When a frame is invisible, it's `elements` will also be invisible. Deleting a frame will also delete it's `elements`.

### Frame Path

A frame path is a string representation of the route to a certain frame.

Say we have the following json file
```json
{
   "Arthur": {
      "type": "frame"
      "contents": {
         "Bertha": {
            "type": "frame"
            "contents": {
               "Pippinpaddleopsicopolis": {
                  "type": "frame"
               }
            }
         },
         "Cedric": {
            "type": "frame"
         }
      }
   }
}
```

and i wanted to access `Pippinpaddleopsicopolis`

The syntax for the frame path is very simple:
```python
"Arthur->Bertha->Pippinpaddleopsicopolis"
```

## Examples

All examples use [this](#python-file) python file as base.

### A button

```json
{
   "harry the button": {
      "type": "button",
      "position": [250,120],
      "size": [200,200],
      "background_color": [100,0,0],
      "contents": {
         "jonathan the label": {
            "type": "label",
            "position": [260,150],
            "font_size": 30,
            "auto_size": true
         }
      }
   }
}
```
With this called after `pygame_ui.init()`:
```python
harry = Interface.get_element('harry the button', 'frame1->frame2')
jonathan = Interface.get_element('jonathan the label', 'frame1->frame2->harry the button')
```
And this between `event_handler()` and `draw()`:
```python
jonathan.text = "start: "+str(harry.click_start)+", end: "+str(harry.click_end)+", held: "+str(harry.held)
```


### Adding An Element Post Initialization

```python
play_label = pygame_ui.label(position=[100,100], size=[100,100], text="play now", text_size=20)
Interface.add_element('play', play_label)
```

### Adding An Element To A Frame

```python
play_label = pygame_ui.label(position=[100,100], size=[100,100], text="play now", text_size=20)
Interface.add_element('play', play_label, 'Arthur->Bertha->Pippinpaddleopsicopolis')
```

### Removing An Element From A Frame

```python
Interface.remove_element('Pippinpaddleopsicopolis', 'Arthur->Bertha')
```

### Get Element Object
```python
play_label = Interface.get_element('play', 'Arthur->Bertha->Pippinpaddleopsicopolis')
play_label.text = 'THE THIRD'
```

### Frame-ception

Just... don't ask me why.

#### Python
```python
import pygame
import pygame_ui

pygame.init()
screen = pygame.display.set_mode((1280, 720), vsync=1)
pygame.display.set_caption("Frame-ception")
clock = pygame.time.Clock()

Interface = pygame_ui.init()

path = 'frame0'
for i in range(100):
   frame = 'frame'+str(i+1)
   Interface.add_element(frame, pygame_ui.frame(), path)
   path += '->'+frame

while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         quit()

   screen.fill((0,0,0))

   Interface.draw(screen)

   pygame.display.flip()
   clock.tick(60)
```

#### JSON
```json
{
   "frame0": {
      "type": "frame",
      "contents": {}
   }
}
```

## FAQ

Nothing yet lol.