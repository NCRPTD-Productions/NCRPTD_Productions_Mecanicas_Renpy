init python:
    
    # Shader code
    wave_shader = """
        uniform float time;         // Time variable for animation
        uniform float speed;        // Speed of the wave
        uniform float amplitude;    // Amplitude of the wave
        uniform float frequency;    // Frequency of the wave
        
        void main() {
            // Get the pixel coordinates, normalized to [0, 1]
            vec2 coords = gl_FragCoord.xy / iResolution.xy;
            
            // Create a sine wave effect based on the y-coordinate and time
            float wave = sin(coords.y * frequency + time * speed) * amplitude;
            
            // Distort the texture based on the wave
            vec2 new_coords = coords + vec2(wave, 0.0);
            
            // Sample the texture at the new distorted coordinates
            gl_FragColor = texture(iChannel0, new_coords);
        }
    """
    
    # Register the shader
    renpy.shaders.register_shader("example.waves", variables='''
    uniform float time;
    uniform float speed;
    uniform float amplitude;
    uniform float frequency;
    ''')
