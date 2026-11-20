import AppKit
let args = CommandLine.arguments
let size = CGFloat(Int(args[1])!), out = args[2]
let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: Int(size), pixelsHigh: Int(size), bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false, colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
NSGraphicsContext.saveGraphicsState()
NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: rep)
let rect = NSRect(x: 0, y: 0, width: size, height: size)
let g = NSGradient(starting: NSColor(red: 1, green: 0.84, blue: 0.93, alpha: 1), ending: NSColor(red: 0.85, green: 0.76, blue: 1, alpha: 1))!
g.draw(in: rect, angle: -90)
let s = "📖" as NSString
let font = NSFont.systemFont(ofSize: size * 0.62)
let attrs: [NSAttributedString.Key: Any] = [.font: font]
let ts = s.size(withAttributes: attrs)
s.draw(at: NSPoint(x: (size - ts.width) / 2, y: (size - ts.height) / 2), withAttributes: attrs)
NSGraphicsContext.restoreGraphicsState()
try! rep.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: out))
