This is your new *vault*.

Make a note of something, [[create a link]], or try [the Importer](https://help.obsidian.md/Plugins/Importer)!

When you're ready, delete this note and make the vault your own.

```markdown
# Heading 1
## Heading 2
...

**Bold text** //note that hotkeys like ctrl-b also work
*Italic text* //note that hotkeys like ctrl-i also work

- Bullet points
- Like this

1. Numbered lists
2. Like this

> Blockquotes like this

[[Internal links]] to other notes (!)

[[Internal links with alias|Alias]] //the link is displayed with alias text rather than original text

[External links](https://example.com)

![Images](path/to/image.jpg)

> [!callout type] Callout Title
> Callout content

—- horizontal dividing lines
```


## Internal links

Obsidian supports two formats for [internal links](https://help.obsidian.md/links) between notes:

- Wikilink: `[[Three laws of motion]]`
- Markdown: `[Three laws of motion](Three%20laws%20of%20motion.md)`


## External links

If you want to link to an external URL, you can create an inline link by surrounding the link text in brackets (`[ ]`), and then the URL in parentheses (`( )`).

```md
[Obsidian Help](https://help.obsidian.md)
```

[Obsidian Help](https://help.obsidian.md)

You can also create external links to files in other vaults, by linking to an [Obsidian URI](https://help.obsidian.md/Extending+Obsidian/Obsidian+URI).

```md
[Note](obsidian://open?vault=MainVault&file=Note.md)
```

### Escape blank spaces in links

If your URL contains blank spaces, you must escape them by replacing them with `%20`.

```md
[My Note](obsidian://open?vault=MainVault&file=My%20Note.md)
```

You can also escape the URL by wrapping it with angled brackets (`< >`).

```md
[My Note](<obsidian://open?vault=MainVault&file=My Note.md>)
```
