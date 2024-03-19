# trace generated using paraview version 5.11.2
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
import os
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Xdmf3ReaderS'
classicxdmf = Xdmf3ReaderS(registrationName='Classic.xdmf', FileName=[os.getcwd() + '/UnitCube/Newton/output/Classic.xdmf'])
classicxdmf.PointArrays = ['f_55']
classicxdmf.CellArrays = []
classicxdmf.Sets = []

# get animation scene
animationScene1 = GetAnimationScene()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# create a new 'PVD Reader'
initial_cubepvd = PVDReader(registrationName='initial_cube.pvd', FileName=os.getcwd() + '/UnitCube/initial_cube.pvd')
initial_cubepvd.CellArrays = []
initial_cubepvd.PointArrays = ['f_28']
initial_cubepvd.ColumnArrays = []

# create a new 'STL Reader'
cube_deletedstl = STLReader(registrationName='cube_deleted.stl', FileNames=[os.getcwd() + '/UnitCube/cube_deleted.stl'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
initial_cubepvdDisplay = Show(initial_cubepvd, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'f_28'
f_28LUT = GetColorTransferFunction('f_28')

# get opacity transfer function/opacity map for 'f_28'
f_28PWF = GetOpacityTransferFunction('f_28')

# trace defaults for the display properties.
initial_cubepvdDisplay.Selection = None
initial_cubepvdDisplay.Representation = 'Surface'
initial_cubepvdDisplay.ColorArrayName = ['POINTS', 'f_28']
initial_cubepvdDisplay.LookupTable = f_28LUT
initial_cubepvdDisplay.MapScalars = 1
initial_cubepvdDisplay.MultiComponentsMapping = 0
initial_cubepvdDisplay.InterpolateScalarsBeforeMapping = 1
initial_cubepvdDisplay.Opacity = 1.0
initial_cubepvdDisplay.PointSize = 2.0
initial_cubepvdDisplay.LineWidth = 1.0
initial_cubepvdDisplay.RenderLinesAsTubes = 0
initial_cubepvdDisplay.RenderPointsAsSpheres = 0
initial_cubepvdDisplay.Interpolation = 'Gouraud'
initial_cubepvdDisplay.Specular = 0.0
initial_cubepvdDisplay.SpecularColor = [1.0, 1.0, 1.0]
initial_cubepvdDisplay.SpecularPower = 100.0
initial_cubepvdDisplay.Luminosity = 0.0
initial_cubepvdDisplay.Ambient = 0.0
initial_cubepvdDisplay.Diffuse = 1.0
initial_cubepvdDisplay.Roughness = 0.3
initial_cubepvdDisplay.Metallic = 0.0
initial_cubepvdDisplay.EdgeTint = [1.0, 1.0, 1.0]
initial_cubepvdDisplay.Anisotropy = 0.0
initial_cubepvdDisplay.AnisotropyRotation = 0.0
initial_cubepvdDisplay.BaseIOR = 1.5
initial_cubepvdDisplay.CoatStrength = 0.0
initial_cubepvdDisplay.CoatIOR = 2.0
initial_cubepvdDisplay.CoatRoughness = 0.0
initial_cubepvdDisplay.CoatColor = [1.0, 1.0, 1.0]
initial_cubepvdDisplay.SelectTCoordArray = 'None'
initial_cubepvdDisplay.SelectNormalArray = 'None'
initial_cubepvdDisplay.SelectTangentArray = 'None'
initial_cubepvdDisplay.Texture = None
initial_cubepvdDisplay.RepeatTextures = 1
initial_cubepvdDisplay.InterpolateTextures = 0
initial_cubepvdDisplay.SeamlessU = 0
initial_cubepvdDisplay.SeamlessV = 0
initial_cubepvdDisplay.UseMipmapTextures = 0
initial_cubepvdDisplay.ShowTexturesOnBackface = 1
initial_cubepvdDisplay.BaseColorTexture = None
initial_cubepvdDisplay.NormalTexture = None
initial_cubepvdDisplay.NormalScale = 1.0
initial_cubepvdDisplay.CoatNormalTexture = None
initial_cubepvdDisplay.CoatNormalScale = 1.0
initial_cubepvdDisplay.MaterialTexture = None
initial_cubepvdDisplay.OcclusionStrength = 1.0
initial_cubepvdDisplay.AnisotropyTexture = None
initial_cubepvdDisplay.EmissiveTexture = None
initial_cubepvdDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
initial_cubepvdDisplay.FlipTextures = 0
initial_cubepvdDisplay.BackfaceRepresentation = 'Follow Frontface'
initial_cubepvdDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
initial_cubepvdDisplay.BackfaceOpacity = 1.0
initial_cubepvdDisplay.Position = [0.0, 0.0, 0.0]
initial_cubepvdDisplay.Scale = [1.0, 1.0, 1.0]
initial_cubepvdDisplay.Orientation = [0.0, 0.0, 0.0]
initial_cubepvdDisplay.Origin = [0.0, 0.0, 0.0]
initial_cubepvdDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
initial_cubepvdDisplay.Pickable = 1
initial_cubepvdDisplay.Triangulate = 0
initial_cubepvdDisplay.UseShaderReplacements = 0
initial_cubepvdDisplay.ShaderReplacements = ''
initial_cubepvdDisplay.NonlinearSubdivisionLevel = 1
initial_cubepvdDisplay.UseDataPartitions = 0
initial_cubepvdDisplay.OSPRayUseScaleArray = 'All Approximate'
initial_cubepvdDisplay.OSPRayScaleArray = 'f_28'
initial_cubepvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
initial_cubepvdDisplay.OSPRayMaterial = 'None'
initial_cubepvdDisplay.BlockSelectors = ['/']
initial_cubepvdDisplay.BlockColors = []
initial_cubepvdDisplay.BlockOpacities = []
initial_cubepvdDisplay.Orient = 0
initial_cubepvdDisplay.OrientationMode = 'Direction'
initial_cubepvdDisplay.SelectOrientationVectors = 'None'
initial_cubepvdDisplay.Scaling = 0
initial_cubepvdDisplay.ScaleMode = 'No Data Scaling Off'
initial_cubepvdDisplay.ScaleFactor = 0.1
initial_cubepvdDisplay.SelectScaleArray = 'f_28'
initial_cubepvdDisplay.GlyphType = 'Arrow'
initial_cubepvdDisplay.UseGlyphTable = 0
initial_cubepvdDisplay.GlyphTableIndexArray = 'f_28'
initial_cubepvdDisplay.UseCompositeGlyphTable = 0
initial_cubepvdDisplay.UseGlyphCullingAndLOD = 0
initial_cubepvdDisplay.LODValues = []
initial_cubepvdDisplay.ColorByLODIndex = 0
initial_cubepvdDisplay.GaussianRadius = 0.005
initial_cubepvdDisplay.ShaderPreset = 'Sphere'
initial_cubepvdDisplay.CustomTriangleScale = 3
initial_cubepvdDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
initial_cubepvdDisplay.Emissive = 0
initial_cubepvdDisplay.ScaleByArray = 0
initial_cubepvdDisplay.SetScaleArray = ['POINTS', 'f_28']
initial_cubepvdDisplay.ScaleArrayComponent = ''
initial_cubepvdDisplay.UseScaleFunction = 1
initial_cubepvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
initial_cubepvdDisplay.OpacityByArray = 0
initial_cubepvdDisplay.OpacityArray = ['POINTS', 'f_28']
initial_cubepvdDisplay.OpacityArrayComponent = ''
initial_cubepvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
initial_cubepvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
initial_cubepvdDisplay.SelectionCellLabelBold = 0
initial_cubepvdDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
initial_cubepvdDisplay.SelectionCellLabelFontFamily = 'Arial'
initial_cubepvdDisplay.SelectionCellLabelFontFile = ''
initial_cubepvdDisplay.SelectionCellLabelFontSize = 18
initial_cubepvdDisplay.SelectionCellLabelItalic = 0
initial_cubepvdDisplay.SelectionCellLabelJustification = 'Left'
initial_cubepvdDisplay.SelectionCellLabelOpacity = 1.0
initial_cubepvdDisplay.SelectionCellLabelShadow = 0
initial_cubepvdDisplay.SelectionPointLabelBold = 0
initial_cubepvdDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
initial_cubepvdDisplay.SelectionPointLabelFontFamily = 'Arial'
initial_cubepvdDisplay.SelectionPointLabelFontFile = ''
initial_cubepvdDisplay.SelectionPointLabelFontSize = 18
initial_cubepvdDisplay.SelectionPointLabelItalic = 0
initial_cubepvdDisplay.SelectionPointLabelJustification = 'Left'
initial_cubepvdDisplay.SelectionPointLabelOpacity = 1.0
initial_cubepvdDisplay.SelectionPointLabelShadow = 0
initial_cubepvdDisplay.PolarAxes = 'PolarAxesRepresentation'
initial_cubepvdDisplay.ScalarOpacityFunction = f_28PWF
initial_cubepvdDisplay.ScalarOpacityUnitDistance = 0.15789534152309156
initial_cubepvdDisplay.UseSeparateOpacityArray = 0
initial_cubepvdDisplay.OpacityArrayName = ['POINTS', 'f_28']
initial_cubepvdDisplay.OpacityComponent = ''
initial_cubepvdDisplay.SelectMapper = 'Projected tetra'
initial_cubepvdDisplay.SamplingDimensions = [128, 128, 128]
initial_cubepvdDisplay.UseFloatingPointFrameBuffer = 1
initial_cubepvdDisplay.SelectInputVectors = [None, '']
initial_cubepvdDisplay.NumberOfSteps = 40
initial_cubepvdDisplay.StepSize = 0.25
initial_cubepvdDisplay.NormalizeVectors = 1
initial_cubepvdDisplay.EnhancedLIC = 1
initial_cubepvdDisplay.ColorMode = 'Blend'
initial_cubepvdDisplay.LICIntensity = 0.8
initial_cubepvdDisplay.MapModeBias = 0.0
initial_cubepvdDisplay.EnhanceContrast = 'Off'
initial_cubepvdDisplay.LowLICContrastEnhancementFactor = 0.0
initial_cubepvdDisplay.HighLICContrastEnhancementFactor = 0.0
initial_cubepvdDisplay.LowColorContrastEnhancementFactor = 0.0
initial_cubepvdDisplay.HighColorContrastEnhancementFactor = 0.0
initial_cubepvdDisplay.AntiAlias = 0
initial_cubepvdDisplay.MaskOnSurface = 1
initial_cubepvdDisplay.MaskThreshold = 0.0
initial_cubepvdDisplay.MaskIntensity = 0.0
initial_cubepvdDisplay.MaskColor = [0.5, 0.5, 0.5]
initial_cubepvdDisplay.GenerateNoiseTexture = 0
initial_cubepvdDisplay.NoiseType = 'Gaussian'
initial_cubepvdDisplay.NoiseTextureSize = 128
initial_cubepvdDisplay.NoiseGrainSize = 2
initial_cubepvdDisplay.MinNoiseValue = 0.0
initial_cubepvdDisplay.MaxNoiseValue = 0.8
initial_cubepvdDisplay.NumberOfNoiseLevels = 1024
initial_cubepvdDisplay.ImpulseNoiseProbability = 1.0
initial_cubepvdDisplay.ImpulseNoiseBackgroundValue = 0.0
initial_cubepvdDisplay.NoiseGeneratorSeed = 1
initial_cubepvdDisplay.CompositeStrategy = 'AUTO'
initial_cubepvdDisplay.UseLICForLOD = 0
initial_cubepvdDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
initial_cubepvdDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
initial_cubepvdDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
initial_cubepvdDisplay.GlyphType.TipResolution = 6
initial_cubepvdDisplay.GlyphType.TipRadius = 0.1
initial_cubepvdDisplay.GlyphType.TipLength = 0.35
initial_cubepvdDisplay.GlyphType.ShaftResolution = 6
initial_cubepvdDisplay.GlyphType.ShaftRadius = 0.03
initial_cubepvdDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
initial_cubepvdDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
initial_cubepvdDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
initial_cubepvdDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
initial_cubepvdDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
initial_cubepvdDisplay.DataAxesGrid.XTitle = 'X Axis'
initial_cubepvdDisplay.DataAxesGrid.YTitle = 'Y Axis'
initial_cubepvdDisplay.DataAxesGrid.ZTitle = 'Z Axis'
initial_cubepvdDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
initial_cubepvdDisplay.DataAxesGrid.XTitleFontFile = ''
initial_cubepvdDisplay.DataAxesGrid.XTitleBold = 0
initial_cubepvdDisplay.DataAxesGrid.XTitleItalic = 0
initial_cubepvdDisplay.DataAxesGrid.XTitleFontSize = 12
initial_cubepvdDisplay.DataAxesGrid.XTitleShadow = 0
initial_cubepvdDisplay.DataAxesGrid.XTitleOpacity = 1.0
initial_cubepvdDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
initial_cubepvdDisplay.DataAxesGrid.YTitleFontFile = ''
initial_cubepvdDisplay.DataAxesGrid.YTitleBold = 0
initial_cubepvdDisplay.DataAxesGrid.YTitleItalic = 0
initial_cubepvdDisplay.DataAxesGrid.YTitleFontSize = 12
initial_cubepvdDisplay.DataAxesGrid.YTitleShadow = 0
initial_cubepvdDisplay.DataAxesGrid.YTitleOpacity = 1.0
initial_cubepvdDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
initial_cubepvdDisplay.DataAxesGrid.ZTitleFontFile = ''
initial_cubepvdDisplay.DataAxesGrid.ZTitleBold = 0
initial_cubepvdDisplay.DataAxesGrid.ZTitleItalic = 0
initial_cubepvdDisplay.DataAxesGrid.ZTitleFontSize = 12
initial_cubepvdDisplay.DataAxesGrid.ZTitleShadow = 0
initial_cubepvdDisplay.DataAxesGrid.ZTitleOpacity = 1.0
initial_cubepvdDisplay.DataAxesGrid.FacesToRender = 63
initial_cubepvdDisplay.DataAxesGrid.CullBackface = 0
initial_cubepvdDisplay.DataAxesGrid.CullFrontface = 1
initial_cubepvdDisplay.DataAxesGrid.ShowGrid = 0
initial_cubepvdDisplay.DataAxesGrid.ShowEdges = 1
initial_cubepvdDisplay.DataAxesGrid.ShowTicks = 1
initial_cubepvdDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
initial_cubepvdDisplay.DataAxesGrid.AxesToLabel = 63
initial_cubepvdDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
initial_cubepvdDisplay.DataAxesGrid.XLabelFontFile = ''
initial_cubepvdDisplay.DataAxesGrid.XLabelBold = 0
initial_cubepvdDisplay.DataAxesGrid.XLabelItalic = 0
initial_cubepvdDisplay.DataAxesGrid.XLabelFontSize = 12
initial_cubepvdDisplay.DataAxesGrid.XLabelShadow = 0
initial_cubepvdDisplay.DataAxesGrid.XLabelOpacity = 1.0
initial_cubepvdDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
initial_cubepvdDisplay.DataAxesGrid.YLabelFontFile = ''
initial_cubepvdDisplay.DataAxesGrid.YLabelBold = 0
initial_cubepvdDisplay.DataAxesGrid.YLabelItalic = 0
initial_cubepvdDisplay.DataAxesGrid.YLabelFontSize = 12
initial_cubepvdDisplay.DataAxesGrid.YLabelShadow = 0
initial_cubepvdDisplay.DataAxesGrid.YLabelOpacity = 1.0
initial_cubepvdDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
initial_cubepvdDisplay.DataAxesGrid.ZLabelFontFile = ''
initial_cubepvdDisplay.DataAxesGrid.ZLabelBold = 0
initial_cubepvdDisplay.DataAxesGrid.ZLabelItalic = 0
initial_cubepvdDisplay.DataAxesGrid.ZLabelFontSize = 12
initial_cubepvdDisplay.DataAxesGrid.ZLabelShadow = 0
initial_cubepvdDisplay.DataAxesGrid.ZLabelOpacity = 1.0
initial_cubepvdDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
initial_cubepvdDisplay.DataAxesGrid.XAxisPrecision = 2
initial_cubepvdDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
initial_cubepvdDisplay.DataAxesGrid.XAxisLabels = []
initial_cubepvdDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
initial_cubepvdDisplay.DataAxesGrid.YAxisPrecision = 2
initial_cubepvdDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
initial_cubepvdDisplay.DataAxesGrid.YAxisLabels = []
initial_cubepvdDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
initial_cubepvdDisplay.DataAxesGrid.ZAxisPrecision = 2
initial_cubepvdDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
initial_cubepvdDisplay.DataAxesGrid.ZAxisLabels = []
initial_cubepvdDisplay.DataAxesGrid.UseCustomBounds = 0
initial_cubepvdDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
initial_cubepvdDisplay.PolarAxes.Visibility = 0
initial_cubepvdDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
initial_cubepvdDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
initial_cubepvdDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
initial_cubepvdDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
initial_cubepvdDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
initial_cubepvdDisplay.PolarAxes.EnableCustomRange = 0
initial_cubepvdDisplay.PolarAxes.CustomRange = [0.0, 1.0]
initial_cubepvdDisplay.PolarAxes.PolarAxisVisibility = 1
initial_cubepvdDisplay.PolarAxes.RadialAxesVisibility = 1
initial_cubepvdDisplay.PolarAxes.DrawRadialGridlines = 1
initial_cubepvdDisplay.PolarAxes.PolarArcsVisibility = 1
initial_cubepvdDisplay.PolarAxes.DrawPolarArcsGridlines = 1
initial_cubepvdDisplay.PolarAxes.NumberOfRadialAxes = 0
initial_cubepvdDisplay.PolarAxes.AutoSubdividePolarAxis = 1
initial_cubepvdDisplay.PolarAxes.NumberOfPolarAxis = 0
initial_cubepvdDisplay.PolarAxes.MinimumRadius = 0.0
initial_cubepvdDisplay.PolarAxes.MinimumAngle = 0.0
initial_cubepvdDisplay.PolarAxes.MaximumAngle = 90.0
initial_cubepvdDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
initial_cubepvdDisplay.PolarAxes.Ratio = 1.0
initial_cubepvdDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
initial_cubepvdDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
initial_cubepvdDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
initial_cubepvdDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
initial_cubepvdDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
initial_cubepvdDisplay.PolarAxes.PolarAxisTitleVisibility = 1
initial_cubepvdDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
initial_cubepvdDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
initial_cubepvdDisplay.PolarAxes.PolarLabelVisibility = 1
initial_cubepvdDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
initial_cubepvdDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
initial_cubepvdDisplay.PolarAxes.RadialLabelVisibility = 1
initial_cubepvdDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
initial_cubepvdDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
initial_cubepvdDisplay.PolarAxes.RadialUnitsVisibility = 1
initial_cubepvdDisplay.PolarAxes.ScreenSize = 10.0
initial_cubepvdDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
initial_cubepvdDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
initial_cubepvdDisplay.PolarAxes.PolarAxisTitleFontFile = ''
initial_cubepvdDisplay.PolarAxes.PolarAxisTitleBold = 0
initial_cubepvdDisplay.PolarAxes.PolarAxisTitleItalic = 0
initial_cubepvdDisplay.PolarAxes.PolarAxisTitleShadow = 0
initial_cubepvdDisplay.PolarAxes.PolarAxisTitleFontSize = 12
initial_cubepvdDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
initial_cubepvdDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
initial_cubepvdDisplay.PolarAxes.PolarAxisLabelFontFile = ''
initial_cubepvdDisplay.PolarAxes.PolarAxisLabelBold = 0
initial_cubepvdDisplay.PolarAxes.PolarAxisLabelItalic = 0
initial_cubepvdDisplay.PolarAxes.PolarAxisLabelShadow = 0
initial_cubepvdDisplay.PolarAxes.PolarAxisLabelFontSize = 12
initial_cubepvdDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
initial_cubepvdDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
initial_cubepvdDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
initial_cubepvdDisplay.PolarAxes.LastRadialAxisTextBold = 0
initial_cubepvdDisplay.PolarAxes.LastRadialAxisTextItalic = 0
initial_cubepvdDisplay.PolarAxes.LastRadialAxisTextShadow = 0
initial_cubepvdDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
initial_cubepvdDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
initial_cubepvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
initial_cubepvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
initial_cubepvdDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
initial_cubepvdDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
initial_cubepvdDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
initial_cubepvdDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
initial_cubepvdDisplay.PolarAxes.EnableDistanceLOD = 1
initial_cubepvdDisplay.PolarAxes.DistanceLODThreshold = 0.7
initial_cubepvdDisplay.PolarAxes.EnableViewAngleLOD = 1
initial_cubepvdDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
initial_cubepvdDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
initial_cubepvdDisplay.PolarAxes.PolarTicksVisibility = 1
initial_cubepvdDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
initial_cubepvdDisplay.PolarAxes.TickLocation = 'Both'
initial_cubepvdDisplay.PolarAxes.AxisTickVisibility = 1
initial_cubepvdDisplay.PolarAxes.AxisMinorTickVisibility = 0
initial_cubepvdDisplay.PolarAxes.ArcTickVisibility = 1
initial_cubepvdDisplay.PolarAxes.ArcMinorTickVisibility = 0
initial_cubepvdDisplay.PolarAxes.DeltaAngleMajor = 10.0
initial_cubepvdDisplay.PolarAxes.DeltaAngleMinor = 5.0
initial_cubepvdDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
initial_cubepvdDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
initial_cubepvdDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
initial_cubepvdDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
initial_cubepvdDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
initial_cubepvdDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
initial_cubepvdDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
initial_cubepvdDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
initial_cubepvdDisplay.PolarAxes.ArcMajorTickSize = 0.0
initial_cubepvdDisplay.PolarAxes.ArcTickRatioSize = 0.3
initial_cubepvdDisplay.PolarAxes.ArcMajorTickThickness = 1.0
initial_cubepvdDisplay.PolarAxes.ArcTickRatioThickness = 0.5
initial_cubepvdDisplay.PolarAxes.Use2DMode = 0
initial_cubepvdDisplay.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
initial_cubepvdDisplay.SetScalarBarVisibility(renderView1, True)

# show data in view
classicxdmfDisplay = Show(classicxdmf, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
classicxdmfDisplay.Selection = None
classicxdmfDisplay.Representation = 'Surface'
classicxdmfDisplay.ColorArrayName = [None, '']
classicxdmfDisplay.LookupTable = None
classicxdmfDisplay.MapScalars = 1
classicxdmfDisplay.MultiComponentsMapping = 0
classicxdmfDisplay.InterpolateScalarsBeforeMapping = 1
classicxdmfDisplay.Opacity = 1.0
classicxdmfDisplay.PointSize = 2.0
classicxdmfDisplay.LineWidth = 1.0
classicxdmfDisplay.RenderLinesAsTubes = 0
classicxdmfDisplay.RenderPointsAsSpheres = 0
classicxdmfDisplay.Interpolation = 'Gouraud'
classicxdmfDisplay.Specular = 0.0
classicxdmfDisplay.SpecularColor = [1.0, 1.0, 1.0]
classicxdmfDisplay.SpecularPower = 100.0
classicxdmfDisplay.Luminosity = 0.0
classicxdmfDisplay.Ambient = 0.0
classicxdmfDisplay.Diffuse = 1.0
classicxdmfDisplay.Roughness = 0.3
classicxdmfDisplay.Metallic = 0.0
classicxdmfDisplay.EdgeTint = [1.0, 1.0, 1.0]
classicxdmfDisplay.Anisotropy = 0.0
classicxdmfDisplay.AnisotropyRotation = 0.0
classicxdmfDisplay.BaseIOR = 1.5
classicxdmfDisplay.CoatStrength = 0.0
classicxdmfDisplay.CoatIOR = 2.0
classicxdmfDisplay.CoatRoughness = 0.0
classicxdmfDisplay.CoatColor = [1.0, 1.0, 1.0]
classicxdmfDisplay.SelectTCoordArray = 'None'
classicxdmfDisplay.SelectNormalArray = 'None'
classicxdmfDisplay.SelectTangentArray = 'None'
classicxdmfDisplay.Texture = None
classicxdmfDisplay.RepeatTextures = 1
classicxdmfDisplay.InterpolateTextures = 0
classicxdmfDisplay.SeamlessU = 0
classicxdmfDisplay.SeamlessV = 0
classicxdmfDisplay.UseMipmapTextures = 0
classicxdmfDisplay.ShowTexturesOnBackface = 1
classicxdmfDisplay.BaseColorTexture = None
classicxdmfDisplay.NormalTexture = None
classicxdmfDisplay.NormalScale = 1.0
classicxdmfDisplay.CoatNormalTexture = None
classicxdmfDisplay.CoatNormalScale = 1.0
classicxdmfDisplay.MaterialTexture = None
classicxdmfDisplay.OcclusionStrength = 1.0
classicxdmfDisplay.AnisotropyTexture = None
classicxdmfDisplay.EmissiveTexture = None
classicxdmfDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
classicxdmfDisplay.FlipTextures = 0
classicxdmfDisplay.BackfaceRepresentation = 'Follow Frontface'
classicxdmfDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
classicxdmfDisplay.BackfaceOpacity = 1.0
classicxdmfDisplay.Position = [0.0, 0.0, 0.0]
classicxdmfDisplay.Scale = [1.0, 1.0, 1.0]
classicxdmfDisplay.Orientation = [0.0, 0.0, 0.0]
classicxdmfDisplay.Origin = [0.0, 0.0, 0.0]
classicxdmfDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
classicxdmfDisplay.Pickable = 1
classicxdmfDisplay.Triangulate = 0
classicxdmfDisplay.UseShaderReplacements = 0
classicxdmfDisplay.ShaderReplacements = ''
classicxdmfDisplay.NonlinearSubdivisionLevel = 1
classicxdmfDisplay.UseDataPartitions = 0
classicxdmfDisplay.OSPRayUseScaleArray = 'All Approximate'
classicxdmfDisplay.OSPRayScaleArray = 'f_55'
classicxdmfDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
classicxdmfDisplay.OSPRayMaterial = 'None'
classicxdmfDisplay.BlockSelectors = ['/']
classicxdmfDisplay.BlockColors = []
classicxdmfDisplay.BlockOpacities = []
classicxdmfDisplay.Orient = 0
classicxdmfDisplay.OrientationMode = 'Direction'
classicxdmfDisplay.SelectOrientationVectors = 'f_55'
classicxdmfDisplay.Scaling = 0
classicxdmfDisplay.ScaleMode = 'No Data Scaling Off'
classicxdmfDisplay.ScaleFactor = 0.1
classicxdmfDisplay.SelectScaleArray = 'None'
classicxdmfDisplay.GlyphType = 'Arrow'
classicxdmfDisplay.UseGlyphTable = 0
classicxdmfDisplay.GlyphTableIndexArray = 'None'
classicxdmfDisplay.UseCompositeGlyphTable = 0
classicxdmfDisplay.UseGlyphCullingAndLOD = 0
classicxdmfDisplay.LODValues = []
classicxdmfDisplay.ColorByLODIndex = 0
classicxdmfDisplay.GaussianRadius = 0.005
classicxdmfDisplay.ShaderPreset = 'Sphere'
classicxdmfDisplay.CustomTriangleScale = 3
classicxdmfDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
classicxdmfDisplay.Emissive = 0
classicxdmfDisplay.ScaleByArray = 0
classicxdmfDisplay.SetScaleArray = ['POINTS', 'f_55']
classicxdmfDisplay.ScaleArrayComponent = 'X'
classicxdmfDisplay.UseScaleFunction = 1
classicxdmfDisplay.ScaleTransferFunction = 'PiecewiseFunction'
classicxdmfDisplay.OpacityByArray = 0
classicxdmfDisplay.OpacityArray = ['POINTS', 'f_55']
classicxdmfDisplay.OpacityArrayComponent = 'X'
classicxdmfDisplay.OpacityTransferFunction = 'PiecewiseFunction'
classicxdmfDisplay.DataAxesGrid = 'GridAxesRepresentation'
classicxdmfDisplay.SelectionCellLabelBold = 0
classicxdmfDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
classicxdmfDisplay.SelectionCellLabelFontFamily = 'Arial'
classicxdmfDisplay.SelectionCellLabelFontFile = ''
classicxdmfDisplay.SelectionCellLabelFontSize = 18
classicxdmfDisplay.SelectionCellLabelItalic = 0
classicxdmfDisplay.SelectionCellLabelJustification = 'Left'
classicxdmfDisplay.SelectionCellLabelOpacity = 1.0
classicxdmfDisplay.SelectionCellLabelShadow = 0
classicxdmfDisplay.SelectionPointLabelBold = 0
classicxdmfDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
classicxdmfDisplay.SelectionPointLabelFontFamily = 'Arial'
classicxdmfDisplay.SelectionPointLabelFontFile = ''
classicxdmfDisplay.SelectionPointLabelFontSize = 18
classicxdmfDisplay.SelectionPointLabelItalic = 0
classicxdmfDisplay.SelectionPointLabelJustification = 'Left'
classicxdmfDisplay.SelectionPointLabelOpacity = 1.0
classicxdmfDisplay.SelectionPointLabelShadow = 0
classicxdmfDisplay.PolarAxes = 'PolarAxesRepresentation'
classicxdmfDisplay.ScalarOpacityFunction = None
classicxdmfDisplay.ScalarOpacityUnitDistance = 0.15789534152309156
classicxdmfDisplay.UseSeparateOpacityArray = 0
classicxdmfDisplay.OpacityArrayName = ['POINTS', 'f_55']
classicxdmfDisplay.OpacityComponent = 'X'
classicxdmfDisplay.SelectMapper = 'Projected tetra'
classicxdmfDisplay.SamplingDimensions = [128, 128, 128]
classicxdmfDisplay.UseFloatingPointFrameBuffer = 1
classicxdmfDisplay.SelectInputVectors = ['POINTS', 'f_55']
classicxdmfDisplay.NumberOfSteps = 40
classicxdmfDisplay.StepSize = 0.25
classicxdmfDisplay.NormalizeVectors = 1
classicxdmfDisplay.EnhancedLIC = 1
classicxdmfDisplay.ColorMode = 'Blend'
classicxdmfDisplay.LICIntensity = 0.8
classicxdmfDisplay.MapModeBias = 0.0
classicxdmfDisplay.EnhanceContrast = 'Off'
classicxdmfDisplay.LowLICContrastEnhancementFactor = 0.0
classicxdmfDisplay.HighLICContrastEnhancementFactor = 0.0
classicxdmfDisplay.LowColorContrastEnhancementFactor = 0.0
classicxdmfDisplay.HighColorContrastEnhancementFactor = 0.0
classicxdmfDisplay.AntiAlias = 0
classicxdmfDisplay.MaskOnSurface = 1
classicxdmfDisplay.MaskThreshold = 0.0
classicxdmfDisplay.MaskIntensity = 0.0
classicxdmfDisplay.MaskColor = [0.5, 0.5, 0.5]
classicxdmfDisplay.GenerateNoiseTexture = 0
classicxdmfDisplay.NoiseType = 'Gaussian'
classicxdmfDisplay.NoiseTextureSize = 128
classicxdmfDisplay.NoiseGrainSize = 2
classicxdmfDisplay.MinNoiseValue = 0.0
classicxdmfDisplay.MaxNoiseValue = 0.8
classicxdmfDisplay.NumberOfNoiseLevels = 1024
classicxdmfDisplay.ImpulseNoiseProbability = 1.0
classicxdmfDisplay.ImpulseNoiseBackgroundValue = 0.0
classicxdmfDisplay.NoiseGeneratorSeed = 1
classicxdmfDisplay.CompositeStrategy = 'AUTO'
classicxdmfDisplay.UseLICForLOD = 0
classicxdmfDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
classicxdmfDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
classicxdmfDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
classicxdmfDisplay.GlyphType.TipResolution = 6
classicxdmfDisplay.GlyphType.TipRadius = 0.1
classicxdmfDisplay.GlyphType.TipLength = 0.35
classicxdmfDisplay.GlyphType.ShaftResolution = 6
classicxdmfDisplay.GlyphType.ShaftRadius = 0.03
classicxdmfDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
classicxdmfDisplay.ScaleTransferFunction.Points = [-0.0030061304569244385, 0.0, 0.5, 0.0, 0.002066955203190446, 1.0, 0.5, 0.0]
classicxdmfDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
classicxdmfDisplay.OpacityTransferFunction.Points = [-0.0030061304569244385, 0.0, 0.5, 0.0, 0.002066955203190446, 1.0, 0.5, 0.0]
classicxdmfDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
classicxdmfDisplay.DataAxesGrid.XTitle = 'X Axis'
classicxdmfDisplay.DataAxesGrid.YTitle = 'Y Axis'
classicxdmfDisplay.DataAxesGrid.ZTitle = 'Z Axis'
classicxdmfDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
classicxdmfDisplay.DataAxesGrid.XTitleFontFile = ''
classicxdmfDisplay.DataAxesGrid.XTitleBold = 0
classicxdmfDisplay.DataAxesGrid.XTitleItalic = 0
classicxdmfDisplay.DataAxesGrid.XTitleFontSize = 12
classicxdmfDisplay.DataAxesGrid.XTitleShadow = 0
classicxdmfDisplay.DataAxesGrid.XTitleOpacity = 1.0
classicxdmfDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
classicxdmfDisplay.DataAxesGrid.YTitleFontFile = ''
classicxdmfDisplay.DataAxesGrid.YTitleBold = 0
classicxdmfDisplay.DataAxesGrid.YTitleItalic = 0
classicxdmfDisplay.DataAxesGrid.YTitleFontSize = 12
classicxdmfDisplay.DataAxesGrid.YTitleShadow = 0
classicxdmfDisplay.DataAxesGrid.YTitleOpacity = 1.0
classicxdmfDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
classicxdmfDisplay.DataAxesGrid.ZTitleFontFile = ''
classicxdmfDisplay.DataAxesGrid.ZTitleBold = 0
classicxdmfDisplay.DataAxesGrid.ZTitleItalic = 0
classicxdmfDisplay.DataAxesGrid.ZTitleFontSize = 12
classicxdmfDisplay.DataAxesGrid.ZTitleShadow = 0
classicxdmfDisplay.DataAxesGrid.ZTitleOpacity = 1.0
classicxdmfDisplay.DataAxesGrid.FacesToRender = 63
classicxdmfDisplay.DataAxesGrid.CullBackface = 0
classicxdmfDisplay.DataAxesGrid.CullFrontface = 1
classicxdmfDisplay.DataAxesGrid.ShowGrid = 0
classicxdmfDisplay.DataAxesGrid.ShowEdges = 1
classicxdmfDisplay.DataAxesGrid.ShowTicks = 1
classicxdmfDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
classicxdmfDisplay.DataAxesGrid.AxesToLabel = 63
classicxdmfDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
classicxdmfDisplay.DataAxesGrid.XLabelFontFile = ''
classicxdmfDisplay.DataAxesGrid.XLabelBold = 0
classicxdmfDisplay.DataAxesGrid.XLabelItalic = 0
classicxdmfDisplay.DataAxesGrid.XLabelFontSize = 12
classicxdmfDisplay.DataAxesGrid.XLabelShadow = 0
classicxdmfDisplay.DataAxesGrid.XLabelOpacity = 1.0
classicxdmfDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
classicxdmfDisplay.DataAxesGrid.YLabelFontFile = ''
classicxdmfDisplay.DataAxesGrid.YLabelBold = 0
classicxdmfDisplay.DataAxesGrid.YLabelItalic = 0
classicxdmfDisplay.DataAxesGrid.YLabelFontSize = 12
classicxdmfDisplay.DataAxesGrid.YLabelShadow = 0
classicxdmfDisplay.DataAxesGrid.YLabelOpacity = 1.0
classicxdmfDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
classicxdmfDisplay.DataAxesGrid.ZLabelFontFile = ''
classicxdmfDisplay.DataAxesGrid.ZLabelBold = 0
classicxdmfDisplay.DataAxesGrid.ZLabelItalic = 0
classicxdmfDisplay.DataAxesGrid.ZLabelFontSize = 12
classicxdmfDisplay.DataAxesGrid.ZLabelShadow = 0
classicxdmfDisplay.DataAxesGrid.ZLabelOpacity = 1.0
classicxdmfDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
classicxdmfDisplay.DataAxesGrid.XAxisPrecision = 2
classicxdmfDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
classicxdmfDisplay.DataAxesGrid.XAxisLabels = []
classicxdmfDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
classicxdmfDisplay.DataAxesGrid.YAxisPrecision = 2
classicxdmfDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
classicxdmfDisplay.DataAxesGrid.YAxisLabels = []
classicxdmfDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
classicxdmfDisplay.DataAxesGrid.ZAxisPrecision = 2
classicxdmfDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
classicxdmfDisplay.DataAxesGrid.ZAxisLabels = []
classicxdmfDisplay.DataAxesGrid.UseCustomBounds = 0
classicxdmfDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
classicxdmfDisplay.PolarAxes.Visibility = 0
classicxdmfDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
classicxdmfDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
classicxdmfDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
classicxdmfDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
classicxdmfDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
classicxdmfDisplay.PolarAxes.EnableCustomRange = 0
classicxdmfDisplay.PolarAxes.CustomRange = [0.0, 1.0]
classicxdmfDisplay.PolarAxes.PolarAxisVisibility = 1
classicxdmfDisplay.PolarAxes.RadialAxesVisibility = 1
classicxdmfDisplay.PolarAxes.DrawRadialGridlines = 1
classicxdmfDisplay.PolarAxes.PolarArcsVisibility = 1
classicxdmfDisplay.PolarAxes.DrawPolarArcsGridlines = 1
classicxdmfDisplay.PolarAxes.NumberOfRadialAxes = 0
classicxdmfDisplay.PolarAxes.AutoSubdividePolarAxis = 1
classicxdmfDisplay.PolarAxes.NumberOfPolarAxis = 0
classicxdmfDisplay.PolarAxes.MinimumRadius = 0.0
classicxdmfDisplay.PolarAxes.MinimumAngle = 0.0
classicxdmfDisplay.PolarAxes.MaximumAngle = 90.0
classicxdmfDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
classicxdmfDisplay.PolarAxes.Ratio = 1.0
classicxdmfDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
classicxdmfDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
classicxdmfDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
classicxdmfDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
classicxdmfDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
classicxdmfDisplay.PolarAxes.PolarAxisTitleVisibility = 1
classicxdmfDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
classicxdmfDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
classicxdmfDisplay.PolarAxes.PolarLabelVisibility = 1
classicxdmfDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
classicxdmfDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
classicxdmfDisplay.PolarAxes.RadialLabelVisibility = 1
classicxdmfDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
classicxdmfDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
classicxdmfDisplay.PolarAxes.RadialUnitsVisibility = 1
classicxdmfDisplay.PolarAxes.ScreenSize = 10.0
classicxdmfDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
classicxdmfDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
classicxdmfDisplay.PolarAxes.PolarAxisTitleFontFile = ''
classicxdmfDisplay.PolarAxes.PolarAxisTitleBold = 0
classicxdmfDisplay.PolarAxes.PolarAxisTitleItalic = 0
classicxdmfDisplay.PolarAxes.PolarAxisTitleShadow = 0
classicxdmfDisplay.PolarAxes.PolarAxisTitleFontSize = 12
classicxdmfDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
classicxdmfDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
classicxdmfDisplay.PolarAxes.PolarAxisLabelFontFile = ''
classicxdmfDisplay.PolarAxes.PolarAxisLabelBold = 0
classicxdmfDisplay.PolarAxes.PolarAxisLabelItalic = 0
classicxdmfDisplay.PolarAxes.PolarAxisLabelShadow = 0
classicxdmfDisplay.PolarAxes.PolarAxisLabelFontSize = 12
classicxdmfDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
classicxdmfDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
classicxdmfDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
classicxdmfDisplay.PolarAxes.LastRadialAxisTextBold = 0
classicxdmfDisplay.PolarAxes.LastRadialAxisTextItalic = 0
classicxdmfDisplay.PolarAxes.LastRadialAxisTextShadow = 0
classicxdmfDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
classicxdmfDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
classicxdmfDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
classicxdmfDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
classicxdmfDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
classicxdmfDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
classicxdmfDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
classicxdmfDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
classicxdmfDisplay.PolarAxes.EnableDistanceLOD = 1
classicxdmfDisplay.PolarAxes.DistanceLODThreshold = 0.7
classicxdmfDisplay.PolarAxes.EnableViewAngleLOD = 1
classicxdmfDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
classicxdmfDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
classicxdmfDisplay.PolarAxes.PolarTicksVisibility = 1
classicxdmfDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
classicxdmfDisplay.PolarAxes.TickLocation = 'Both'
classicxdmfDisplay.PolarAxes.AxisTickVisibility = 1
classicxdmfDisplay.PolarAxes.AxisMinorTickVisibility = 0
classicxdmfDisplay.PolarAxes.ArcTickVisibility = 1
classicxdmfDisplay.PolarAxes.ArcMinorTickVisibility = 0
classicxdmfDisplay.PolarAxes.DeltaAngleMajor = 10.0
classicxdmfDisplay.PolarAxes.DeltaAngleMinor = 5.0
classicxdmfDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
classicxdmfDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
classicxdmfDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
classicxdmfDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
classicxdmfDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
classicxdmfDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
classicxdmfDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
classicxdmfDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
classicxdmfDisplay.PolarAxes.ArcMajorTickSize = 0.0
classicxdmfDisplay.PolarAxes.ArcTickRatioSize = 0.3
classicxdmfDisplay.PolarAxes.ArcMajorTickThickness = 1.0
classicxdmfDisplay.PolarAxes.ArcTickRatioThickness = 0.5
classicxdmfDisplay.PolarAxes.Use2DMode = 0
classicxdmfDisplay.PolarAxes.UseLogAxis = 0

# show data in view
cube_deletedstlDisplay = Show(cube_deletedstl, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
cube_deletedstlDisplay.Selection = None
cube_deletedstlDisplay.Representation = 'Surface'
cube_deletedstlDisplay.ColorArrayName = [None, '']
cube_deletedstlDisplay.LookupTable = None
cube_deletedstlDisplay.MapScalars = 1
cube_deletedstlDisplay.MultiComponentsMapping = 0
cube_deletedstlDisplay.InterpolateScalarsBeforeMapping = 1
cube_deletedstlDisplay.Opacity = 1.0
cube_deletedstlDisplay.PointSize = 2.0
cube_deletedstlDisplay.LineWidth = 1.0
cube_deletedstlDisplay.RenderLinesAsTubes = 0
cube_deletedstlDisplay.RenderPointsAsSpheres = 0
cube_deletedstlDisplay.Interpolation = 'Gouraud'
cube_deletedstlDisplay.Specular = 0.0
cube_deletedstlDisplay.SpecularColor = [1.0, 1.0, 1.0]
cube_deletedstlDisplay.SpecularPower = 100.0
cube_deletedstlDisplay.Luminosity = 0.0
cube_deletedstlDisplay.Ambient = 0.0
cube_deletedstlDisplay.Diffuse = 1.0
cube_deletedstlDisplay.Roughness = 0.3
cube_deletedstlDisplay.Metallic = 0.0
cube_deletedstlDisplay.EdgeTint = [1.0, 1.0, 1.0]
cube_deletedstlDisplay.Anisotropy = 0.0
cube_deletedstlDisplay.AnisotropyRotation = 0.0
cube_deletedstlDisplay.BaseIOR = 1.5
cube_deletedstlDisplay.CoatStrength = 0.0
cube_deletedstlDisplay.CoatIOR = 2.0
cube_deletedstlDisplay.CoatRoughness = 0.0
cube_deletedstlDisplay.CoatColor = [1.0, 1.0, 1.0]
cube_deletedstlDisplay.SelectTCoordArray = 'None'
cube_deletedstlDisplay.SelectNormalArray = 'None'
cube_deletedstlDisplay.SelectTangentArray = 'None'
cube_deletedstlDisplay.Texture = None
cube_deletedstlDisplay.RepeatTextures = 1
cube_deletedstlDisplay.InterpolateTextures = 0
cube_deletedstlDisplay.SeamlessU = 0
cube_deletedstlDisplay.SeamlessV = 0
cube_deletedstlDisplay.UseMipmapTextures = 0
cube_deletedstlDisplay.ShowTexturesOnBackface = 1
cube_deletedstlDisplay.BaseColorTexture = None
cube_deletedstlDisplay.NormalTexture = None
cube_deletedstlDisplay.NormalScale = 1.0
cube_deletedstlDisplay.CoatNormalTexture = None
cube_deletedstlDisplay.CoatNormalScale = 1.0
cube_deletedstlDisplay.MaterialTexture = None
cube_deletedstlDisplay.OcclusionStrength = 1.0
cube_deletedstlDisplay.AnisotropyTexture = None
cube_deletedstlDisplay.EmissiveTexture = None
cube_deletedstlDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
cube_deletedstlDisplay.FlipTextures = 0
cube_deletedstlDisplay.BackfaceRepresentation = 'Follow Frontface'
cube_deletedstlDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
cube_deletedstlDisplay.BackfaceOpacity = 1.0
cube_deletedstlDisplay.Position = [0.0, 0.0, 0.0]
cube_deletedstlDisplay.Scale = [1.0, 1.0, 1.0]
cube_deletedstlDisplay.Orientation = [0.0, 0.0, 0.0]
cube_deletedstlDisplay.Origin = [0.0, 0.0, 0.0]
cube_deletedstlDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
cube_deletedstlDisplay.Pickable = 1
cube_deletedstlDisplay.Triangulate = 0
cube_deletedstlDisplay.UseShaderReplacements = 0
cube_deletedstlDisplay.ShaderReplacements = ''
cube_deletedstlDisplay.NonlinearSubdivisionLevel = 1
cube_deletedstlDisplay.UseDataPartitions = 0
cube_deletedstlDisplay.OSPRayUseScaleArray = 'All Approximate'
cube_deletedstlDisplay.OSPRayScaleArray = ''
cube_deletedstlDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
cube_deletedstlDisplay.OSPRayMaterial = 'None'
cube_deletedstlDisplay.BlockSelectors = ['/']
cube_deletedstlDisplay.BlockColors = []
cube_deletedstlDisplay.BlockOpacities = []
cube_deletedstlDisplay.Orient = 0
cube_deletedstlDisplay.OrientationMode = 'Direction'
cube_deletedstlDisplay.SelectOrientationVectors = 'None'
cube_deletedstlDisplay.Scaling = 0
cube_deletedstlDisplay.ScaleMode = 'No Data Scaling Off'
cube_deletedstlDisplay.ScaleFactor = 0.1
cube_deletedstlDisplay.SelectScaleArray = 'None'
cube_deletedstlDisplay.GlyphType = 'Arrow'
cube_deletedstlDisplay.UseGlyphTable = 0
cube_deletedstlDisplay.GlyphTableIndexArray = 'None'
cube_deletedstlDisplay.UseCompositeGlyphTable = 0
cube_deletedstlDisplay.UseGlyphCullingAndLOD = 0
cube_deletedstlDisplay.LODValues = []
cube_deletedstlDisplay.ColorByLODIndex = 0
cube_deletedstlDisplay.GaussianRadius = 0.005
cube_deletedstlDisplay.ShaderPreset = 'Sphere'
cube_deletedstlDisplay.CustomTriangleScale = 3
cube_deletedstlDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
cube_deletedstlDisplay.Emissive = 0
cube_deletedstlDisplay.ScaleByArray = 0
cube_deletedstlDisplay.SetScaleArray = [None, '']
cube_deletedstlDisplay.ScaleArrayComponent = 0
cube_deletedstlDisplay.UseScaleFunction = 1
cube_deletedstlDisplay.ScaleTransferFunction = 'PiecewiseFunction'
cube_deletedstlDisplay.OpacityByArray = 0
cube_deletedstlDisplay.OpacityArray = [None, '']
cube_deletedstlDisplay.OpacityArrayComponent = 0
cube_deletedstlDisplay.OpacityTransferFunction = 'PiecewiseFunction'
cube_deletedstlDisplay.DataAxesGrid = 'GridAxesRepresentation'
cube_deletedstlDisplay.SelectionCellLabelBold = 0
cube_deletedstlDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
cube_deletedstlDisplay.SelectionCellLabelFontFamily = 'Arial'
cube_deletedstlDisplay.SelectionCellLabelFontFile = ''
cube_deletedstlDisplay.SelectionCellLabelFontSize = 18
cube_deletedstlDisplay.SelectionCellLabelItalic = 0
cube_deletedstlDisplay.SelectionCellLabelJustification = 'Left'
cube_deletedstlDisplay.SelectionCellLabelOpacity = 1.0
cube_deletedstlDisplay.SelectionCellLabelShadow = 0
cube_deletedstlDisplay.SelectionPointLabelBold = 0
cube_deletedstlDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
cube_deletedstlDisplay.SelectionPointLabelFontFamily = 'Arial'
cube_deletedstlDisplay.SelectionPointLabelFontFile = ''
cube_deletedstlDisplay.SelectionPointLabelFontSize = 18
cube_deletedstlDisplay.SelectionPointLabelItalic = 0
cube_deletedstlDisplay.SelectionPointLabelJustification = 'Left'
cube_deletedstlDisplay.SelectionPointLabelOpacity = 1.0
cube_deletedstlDisplay.SelectionPointLabelShadow = 0
cube_deletedstlDisplay.PolarAxes = 'PolarAxesRepresentation'
cube_deletedstlDisplay.SelectInputVectors = [None, '']
cube_deletedstlDisplay.NumberOfSteps = 40
cube_deletedstlDisplay.StepSize = 0.25
cube_deletedstlDisplay.NormalizeVectors = 1
cube_deletedstlDisplay.EnhancedLIC = 1
cube_deletedstlDisplay.ColorMode = 'Blend'
cube_deletedstlDisplay.LICIntensity = 0.8
cube_deletedstlDisplay.MapModeBias = 0.0
cube_deletedstlDisplay.EnhanceContrast = 'Off'
cube_deletedstlDisplay.LowLICContrastEnhancementFactor = 0.0
cube_deletedstlDisplay.HighLICContrastEnhancementFactor = 0.0
cube_deletedstlDisplay.LowColorContrastEnhancementFactor = 0.0
cube_deletedstlDisplay.HighColorContrastEnhancementFactor = 0.0
cube_deletedstlDisplay.AntiAlias = 0
cube_deletedstlDisplay.MaskOnSurface = 1
cube_deletedstlDisplay.MaskThreshold = 0.0
cube_deletedstlDisplay.MaskIntensity = 0.0
cube_deletedstlDisplay.MaskColor = [0.5, 0.5, 0.5]
cube_deletedstlDisplay.GenerateNoiseTexture = 0
cube_deletedstlDisplay.NoiseType = 'Gaussian'
cube_deletedstlDisplay.NoiseTextureSize = 128
cube_deletedstlDisplay.NoiseGrainSize = 2
cube_deletedstlDisplay.MinNoiseValue = 0.0
cube_deletedstlDisplay.MaxNoiseValue = 0.8
cube_deletedstlDisplay.NumberOfNoiseLevels = 1024
cube_deletedstlDisplay.ImpulseNoiseProbability = 1.0
cube_deletedstlDisplay.ImpulseNoiseBackgroundValue = 0.0
cube_deletedstlDisplay.NoiseGeneratorSeed = 1
cube_deletedstlDisplay.CompositeStrategy = 'AUTO'
cube_deletedstlDisplay.UseLICForLOD = 0
cube_deletedstlDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
cube_deletedstlDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
cube_deletedstlDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
cube_deletedstlDisplay.GlyphType.TipResolution = 6
cube_deletedstlDisplay.GlyphType.TipRadius = 0.1
cube_deletedstlDisplay.GlyphType.TipLength = 0.35
cube_deletedstlDisplay.GlyphType.ShaftResolution = 6
cube_deletedstlDisplay.GlyphType.ShaftRadius = 0.03
cube_deletedstlDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cube_deletedstlDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
cube_deletedstlDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cube_deletedstlDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
cube_deletedstlDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
cube_deletedstlDisplay.DataAxesGrid.XTitle = 'X Axis'
cube_deletedstlDisplay.DataAxesGrid.YTitle = 'Y Axis'
cube_deletedstlDisplay.DataAxesGrid.ZTitle = 'Z Axis'
cube_deletedstlDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
cube_deletedstlDisplay.DataAxesGrid.XTitleFontFile = ''
cube_deletedstlDisplay.DataAxesGrid.XTitleBold = 0
cube_deletedstlDisplay.DataAxesGrid.XTitleItalic = 0
cube_deletedstlDisplay.DataAxesGrid.XTitleFontSize = 12
cube_deletedstlDisplay.DataAxesGrid.XTitleShadow = 0
cube_deletedstlDisplay.DataAxesGrid.XTitleOpacity = 1.0
cube_deletedstlDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
cube_deletedstlDisplay.DataAxesGrid.YTitleFontFile = ''
cube_deletedstlDisplay.DataAxesGrid.YTitleBold = 0
cube_deletedstlDisplay.DataAxesGrid.YTitleItalic = 0
cube_deletedstlDisplay.DataAxesGrid.YTitleFontSize = 12
cube_deletedstlDisplay.DataAxesGrid.YTitleShadow = 0
cube_deletedstlDisplay.DataAxesGrid.YTitleOpacity = 1.0
cube_deletedstlDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
cube_deletedstlDisplay.DataAxesGrid.ZTitleFontFile = ''
cube_deletedstlDisplay.DataAxesGrid.ZTitleBold = 0
cube_deletedstlDisplay.DataAxesGrid.ZTitleItalic = 0
cube_deletedstlDisplay.DataAxesGrid.ZTitleFontSize = 12
cube_deletedstlDisplay.DataAxesGrid.ZTitleShadow = 0
cube_deletedstlDisplay.DataAxesGrid.ZTitleOpacity = 1.0
cube_deletedstlDisplay.DataAxesGrid.FacesToRender = 63
cube_deletedstlDisplay.DataAxesGrid.CullBackface = 0
cube_deletedstlDisplay.DataAxesGrid.CullFrontface = 1
cube_deletedstlDisplay.DataAxesGrid.ShowGrid = 0
cube_deletedstlDisplay.DataAxesGrid.ShowEdges = 1
cube_deletedstlDisplay.DataAxesGrid.ShowTicks = 1
cube_deletedstlDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
cube_deletedstlDisplay.DataAxesGrid.AxesToLabel = 63
cube_deletedstlDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
cube_deletedstlDisplay.DataAxesGrid.XLabelFontFile = ''
cube_deletedstlDisplay.DataAxesGrid.XLabelBold = 0
cube_deletedstlDisplay.DataAxesGrid.XLabelItalic = 0
cube_deletedstlDisplay.DataAxesGrid.XLabelFontSize = 12
cube_deletedstlDisplay.DataAxesGrid.XLabelShadow = 0
cube_deletedstlDisplay.DataAxesGrid.XLabelOpacity = 1.0
cube_deletedstlDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
cube_deletedstlDisplay.DataAxesGrid.YLabelFontFile = ''
cube_deletedstlDisplay.DataAxesGrid.YLabelBold = 0
cube_deletedstlDisplay.DataAxesGrid.YLabelItalic = 0
cube_deletedstlDisplay.DataAxesGrid.YLabelFontSize = 12
cube_deletedstlDisplay.DataAxesGrid.YLabelShadow = 0
cube_deletedstlDisplay.DataAxesGrid.YLabelOpacity = 1.0
cube_deletedstlDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
cube_deletedstlDisplay.DataAxesGrid.ZLabelFontFile = ''
cube_deletedstlDisplay.DataAxesGrid.ZLabelBold = 0
cube_deletedstlDisplay.DataAxesGrid.ZLabelItalic = 0
cube_deletedstlDisplay.DataAxesGrid.ZLabelFontSize = 12
cube_deletedstlDisplay.DataAxesGrid.ZLabelShadow = 0
cube_deletedstlDisplay.DataAxesGrid.ZLabelOpacity = 1.0
cube_deletedstlDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
cube_deletedstlDisplay.DataAxesGrid.XAxisPrecision = 2
cube_deletedstlDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
cube_deletedstlDisplay.DataAxesGrid.XAxisLabels = []
cube_deletedstlDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
cube_deletedstlDisplay.DataAxesGrid.YAxisPrecision = 2
cube_deletedstlDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
cube_deletedstlDisplay.DataAxesGrid.YAxisLabels = []
cube_deletedstlDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
cube_deletedstlDisplay.DataAxesGrid.ZAxisPrecision = 2
cube_deletedstlDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
cube_deletedstlDisplay.DataAxesGrid.ZAxisLabels = []
cube_deletedstlDisplay.DataAxesGrid.UseCustomBounds = 0
cube_deletedstlDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
cube_deletedstlDisplay.PolarAxes.Visibility = 0
cube_deletedstlDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
cube_deletedstlDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
cube_deletedstlDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
cube_deletedstlDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
cube_deletedstlDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
cube_deletedstlDisplay.PolarAxes.EnableCustomRange = 0
cube_deletedstlDisplay.PolarAxes.CustomRange = [0.0, 1.0]
cube_deletedstlDisplay.PolarAxes.PolarAxisVisibility = 1
cube_deletedstlDisplay.PolarAxes.RadialAxesVisibility = 1
cube_deletedstlDisplay.PolarAxes.DrawRadialGridlines = 1
cube_deletedstlDisplay.PolarAxes.PolarArcsVisibility = 1
cube_deletedstlDisplay.PolarAxes.DrawPolarArcsGridlines = 1
cube_deletedstlDisplay.PolarAxes.NumberOfRadialAxes = 0
cube_deletedstlDisplay.PolarAxes.AutoSubdividePolarAxis = 1
cube_deletedstlDisplay.PolarAxes.NumberOfPolarAxis = 0
cube_deletedstlDisplay.PolarAxes.MinimumRadius = 0.0
cube_deletedstlDisplay.PolarAxes.MinimumAngle = 0.0
cube_deletedstlDisplay.PolarAxes.MaximumAngle = 90.0
cube_deletedstlDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
cube_deletedstlDisplay.PolarAxes.Ratio = 1.0
cube_deletedstlDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
cube_deletedstlDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
cube_deletedstlDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
cube_deletedstlDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
cube_deletedstlDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
cube_deletedstlDisplay.PolarAxes.PolarAxisTitleVisibility = 1
cube_deletedstlDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
cube_deletedstlDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
cube_deletedstlDisplay.PolarAxes.PolarLabelVisibility = 1
cube_deletedstlDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
cube_deletedstlDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
cube_deletedstlDisplay.PolarAxes.RadialLabelVisibility = 1
cube_deletedstlDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
cube_deletedstlDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
cube_deletedstlDisplay.PolarAxes.RadialUnitsVisibility = 1
cube_deletedstlDisplay.PolarAxes.ScreenSize = 10.0
cube_deletedstlDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
cube_deletedstlDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
cube_deletedstlDisplay.PolarAxes.PolarAxisTitleFontFile = ''
cube_deletedstlDisplay.PolarAxes.PolarAxisTitleBold = 0
cube_deletedstlDisplay.PolarAxes.PolarAxisTitleItalic = 0
cube_deletedstlDisplay.PolarAxes.PolarAxisTitleShadow = 0
cube_deletedstlDisplay.PolarAxes.PolarAxisTitleFontSize = 12
cube_deletedstlDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
cube_deletedstlDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
cube_deletedstlDisplay.PolarAxes.PolarAxisLabelFontFile = ''
cube_deletedstlDisplay.PolarAxes.PolarAxisLabelBold = 0
cube_deletedstlDisplay.PolarAxes.PolarAxisLabelItalic = 0
cube_deletedstlDisplay.PolarAxes.PolarAxisLabelShadow = 0
cube_deletedstlDisplay.PolarAxes.PolarAxisLabelFontSize = 12
cube_deletedstlDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
cube_deletedstlDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
cube_deletedstlDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
cube_deletedstlDisplay.PolarAxes.LastRadialAxisTextBold = 0
cube_deletedstlDisplay.PolarAxes.LastRadialAxisTextItalic = 0
cube_deletedstlDisplay.PolarAxes.LastRadialAxisTextShadow = 0
cube_deletedstlDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
cube_deletedstlDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
cube_deletedstlDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
cube_deletedstlDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
cube_deletedstlDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
cube_deletedstlDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
cube_deletedstlDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
cube_deletedstlDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
cube_deletedstlDisplay.PolarAxes.EnableDistanceLOD = 1
cube_deletedstlDisplay.PolarAxes.DistanceLODThreshold = 0.7
cube_deletedstlDisplay.PolarAxes.EnableViewAngleLOD = 1
cube_deletedstlDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
cube_deletedstlDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
cube_deletedstlDisplay.PolarAxes.PolarTicksVisibility = 1
cube_deletedstlDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
cube_deletedstlDisplay.PolarAxes.TickLocation = 'Both'
cube_deletedstlDisplay.PolarAxes.AxisTickVisibility = 1
cube_deletedstlDisplay.PolarAxes.AxisMinorTickVisibility = 0
cube_deletedstlDisplay.PolarAxes.ArcTickVisibility = 1
cube_deletedstlDisplay.PolarAxes.ArcMinorTickVisibility = 0
cube_deletedstlDisplay.PolarAxes.DeltaAngleMajor = 10.0
cube_deletedstlDisplay.PolarAxes.DeltaAngleMinor = 5.0
cube_deletedstlDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
cube_deletedstlDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
cube_deletedstlDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
cube_deletedstlDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
cube_deletedstlDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
cube_deletedstlDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
cube_deletedstlDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
cube_deletedstlDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
cube_deletedstlDisplay.PolarAxes.ArcMajorTickSize = 0.0
cube_deletedstlDisplay.PolarAxes.ArcTickRatioSize = 0.3
cube_deletedstlDisplay.PolarAxes.ArcMajorTickThickness = 1.0
cube_deletedstlDisplay.PolarAxes.ArcTickRatioThickness = 0.5
cube_deletedstlDisplay.PolarAxes.Use2DMode = 0
cube_deletedstlDisplay.PolarAxes.UseLogAxis = 0

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(initial_cubepvd)

# get 2D transfer function for 'f_28'
f_28TF2D = GetTransferFunction2D('f_28')

# turn off scalar coloring
ColorBy(initial_cubepvdDisplay, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(f_28LUT, renderView1)

animationScene1.GoToLast()

# change representation type
initial_cubepvdDisplay.SetRepresentationType('Surface With Edges')

# change representation type
initial_cubepvdDisplay.SetRepresentationType('Surface')

# hide data in view
Hide(initial_cubepvd, renderView1)

# hide data in view
Hide(cube_deletedstl, renderView1)

# change representation type
initial_cubepvdDisplay.SetRepresentationType('Surface With Edges')

# change representation type
initial_cubepvdDisplay.SetRepresentationType('Surface')

# set active source
SetActiveSource(classicxdmf)

# change representation type
classicxdmfDisplay.SetRepresentationType('Surface With Edges')

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(960, 400)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-1.3338464171599922, -0.20183329175447615, -2.2093522789702207]
renderView1.CameraFocalPoint = [0.4999999999999997, 0.49999999999999967, 0.5000000000000003]
renderView1.CameraViewUp = [-0.8348201840003663, 0.1973596453878958, 0.5139303753991963]
renderView1.CameraParallelScale = 0.8660254037844386

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
