from typing import Optional
import flet as ft

class FletSpinkits:
    ROTATING_CIRCLE = "RotatingCircle"
    ROTATING_PLAIN = "RotatingPlain"
    DOUBLE_BOUNCE = "DoubleBounce"
    WAVE = "Wave"
    WANDERING_CUBES = "WanderingCubes"
    FADING_FOUR = "FadingFour"
    FADING_CUBE = "FadingCube"
    PULSE = "Pulse"
    CHASING_DOTS = "ChasingDots"
    THREE_BOUNCE = "ThreeBounce"
    CIRCLE = "Circle"
    CUBE_GRID = "CubeGrid"
    FADING_CIRCLE = "FadingCircle"
    FOLDING_CUBE = "FoldingCube"
    PUMPING_HEART = "PumpingHeart"
    HOUR_GLASS = "HourGlass"
    POURING_HOUR_GLASS = "PouringHourGlass"
    FADING_GRID = "FadingGrid"
    RING = "Ring"
    RIPPLE = "Ripple"
    SPINNING_CIRCLE = "SpinningCircle"
    SPINNING_LINES = "SpinningLines"
    SQUARE_CIRCLE = "SquareCircle"
    DUAL_RING = "DualRing"
    PIANO_WAVE = "PianoWave"
    DANCING_SQUARE = "DancingSquare"
    THREE_IN_OUT = "ThreeInOut"
    WAVE_SPINNER = "WaveSpinner"
    PULSING_GRID = "PulsingGrid"

@ft.control("flet_spinkit")
class FletSpinkit(ft.LayoutControl):
    """
    FletSpinkit Control description.
    """
    # Attaching the constants to the class for easy access
    Spinkits = FletSpinkits

    type: Optional[str] = "RotatingCircle"
    color: Optional[ft.ColorValue] = None
    size: float = 100.00